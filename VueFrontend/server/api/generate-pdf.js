import { defineEventHandler, readBody } from 'h3';
import { jsPDF } from 'jspdf';

export default defineEventHandler(async (event) => {
  try {
    // Read the HTML content from the request body
    const { html } = await readBody(event);
    
    // Log the HTML to ensure it's being received correctly
    console.log('Received HTML:', html);

    // Create a new jsPDF instance
    const pdf = new jsPDF();

    // Convert HTML to PDF
    await pdf.html(html, {
      callback: function (pdf) {
        // Set the response headers for PDF download
        event.res.setHeader('Content-Type', 'application/pdf');
        event.res.setHeader('Content-Disposition', 'attachment; filename="generated.pdf"');

        // Send the PDF as a response
        const pdfBuffer = pdf.output('arraybuffer');
        event.res.end(pdfBuffer); // Finalize the HTTP response
      },
      x: 10,
      y: 10,
    });
  } catch (error) {
    // Log the complete error object for debugging
    console.error('Error generating PDF:', error);
    console.error('Error details:', error.message);
    console.error('Stack trace:', error.stack); // Log the stack trace

    event.res.statusCode = 500; // Internal Server Error
    event.res.end(JSON.stringify({ error: 'Error generating PDF', message: error.message })); // Return the error message
  }
});

