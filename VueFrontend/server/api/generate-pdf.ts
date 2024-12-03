import puppeteer, { Browser, Page } from 'puppeteer';
import { H3Event } from 'h3';

let browserInstance: Browser | null = null;
let pageInstance: Page | null = null;

const getBrowserInstance = async (): Promise<Browser> => {
  if (!browserInstance) {
    browserInstance = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });
  }
  return browserInstance;
};

const getPageInstance = async (): Promise<Page> => {
  if (!pageInstance) {
    const browser = await getBrowserInstance();
    pageInstance = await browser.newPage();
    await pageInstance.setViewport({ width: 2100, height: 2970 });
  }
  return pageInstance;
};

export default defineEventHandler(async (event: H3Event) => {
  try {
    const { html }: { html: string } = await readBody(event);

    if (!html) {
      throw new Error('HTML content is missing');
    }

    // Get the page instance (reuse if already running)
    const page = await getPageInstance();

    // Set content and wait for the DOM to load (faster than networkidle0)
    await page.setContent(html, { waitUntil: 'domcontentloaded' });

    // Inject necessary CSS to handle printing
    await page.addStyleTag({
      content: `
        @page {
          size: A4;
          margin: 20mm;
        }

        body {
          margin: 0;
          padding: 0;
          font-family: Arial, sans-serif;
        }

        .pdf-content {
          width: 100%;
          max-width: 210mm;
          margin: 0 auto;
          padding: 10mm;
          box-sizing: border-box;
        }

        .resume-columns {
          display: flex;
          justify-content: space-between;
          gap: 20px;
        }

        .left-column, .right-column {
          width: 48%;
        }

        .hide-for-print {
          display: none;
        }

        @media print {
          .hide-for-print {
            display: none;
          }
        }

        #title_name {
          text-transform: uppercase !important;
          text-align: center !important;
          font-weight: 800 !important;
        }

        #title_description_job {
          text-transform: capitalize !important;
          text-align: center !important;
        }

        .iconic-section {
          text-align: start !important;
          display: block !important;
          width: auto !important;
          justify-content: space-between !important;
        }

        .row {
          display: flex;
          flex-wrap: wrap;
        }

        .parentTitle {
          columns: 1 !important;
          gap: 10px !important;
          padding: 5px !important;
          margin: 0 !important;
          width: 100% !important;
        }

        .childtitle {
          padding: 5px !important;
          display: inline-block !important;
          width: 100% !important;
        }
      `,
    });

    // Generate the PDF with exact A4 formatting and the required margins
    const pdfBuffer: Uint8Array = await page.pdf({
      format: 'A4',
      margin: {
        top: '20mm',
        right: '20mm',
        bottom: '20mm',
        left: '20mm',
      },
      printBackground: true,
      displayHeaderFooter: false,  // Disable header/footer if not needed for performance
    });

    // Send the PDF as response
    event.node.res.setHeader('Content-Type', 'application/pdf');
    event.node.res.setHeader('Content-Disposition', 'attachment; filename="generated.pdf"');
    event.node.res.end(pdfBuffer);

  } catch (error: unknown) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error';
    console.error('Error generating PDF:', errorMessage);

    // Handle error
    event.node.res.statusCode = 500;
    event.node.res.end(JSON.stringify({
      error: 'Error generating PDF',
      message: errorMessage,
    }));
  }
});
