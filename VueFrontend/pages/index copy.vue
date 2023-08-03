<template>
  <div class="template3">
    <ResumeTemp3.Title />
    <div class="parent">
      <ResumeTemp3.Summary />
      <ResumeTemp3.Skills />
      <ResumeTemp3.Experience />
      <ResumeTemp3.Education />
      <ResumeTemp3.Certification />
      <ResumeTemp3.Frameworks />
      <ResumeTemp3.Programming />
      <ResumeTemp3.Languages />
      <ResumeTemp3.OperatingSystems />
      <ResumeTemp3.Hobbies />
      <ResumeTemp3.Personal_Projects />
      <ResumeTemp3.Reference />
    </div>
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
      <button ref="pdfButton" @click="generatePDF" class="btn btn-success">Download PDF</button>
    </div>
  </div>
</template>

<script >

import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

export default {
  methods: {
    async generatePDF() {
      // Get the printable content
      const content = this.$el;

      // Temporarily hide the button
      this.$refs.pdfButton.style.display = 'none';

      // Create a new jsPDF instance
      const pdf = new jsPDF("p", "mm", "a4");

      // Convert HTML to canvas
      try {
        const canvas = await html2canvas(content, { scale: '1' });

        // Add canvas image to the PDF
        const imageData = canvas.toDataURL('image/png');
        // pdf.addImage(imageData, 'PNG', 15, 15, 180, 0);

        // Save the PDF
        // pdf.save('kimeli_ronald_resume.pdf');

        // pdf.setFont('Arial');
        // pdf.getFontSize(11);
        // pdf.addImage(imageData, 'PNG', 0, 0, width, height);
        // pdf.save();

        // const pdfWidth = pdf.internal.pageSize.getWidth();
        // const pdfHeight = pdf.internal.pageSize.getHeight();
        // pdf.addImage(imageData, 'PNG', 0, 0, pdfWidth, pdfHeight);
        // pdf.save('download.pdf');

        const imgProps = pdf.getImageProperties(imageData);
        const margin = 0;

        const pdfWidth = pdf.internal.pageSize.width * (1 - margin);
        const pdfHeight = pdf.internal.pageSize.height * (1 - margin);

        const x = pdf.internal.pageSize.width * (margin / 2);
        const y = pdf.internal.pageSize.height * (margin / 2);

        const widthRatio = pdfWidth / imgProps.width;
        const heightRatio = pdfHeight / imgProps.height;

        const ratio = Math.min(widthRatio, heightRatio);

        const w = imgProps.width * ratio;
        const h = imgProps.height * ratio;

        pdf.addImage(imageData, "PNG", x, y, w, h, undefined, 'FAST');

        pdf.setFont('Garamond', 'normal');
        pdf.setFontSize(12);

        pdf.save();

      } catch (error) {
        console.error('Error generating PDF:', error);
      } finally {
        // Restore the button's display property
        this.$refs.pdfButton.style.display = '';
      }
    },
  },
};

useHead({
  title: 'Resume Builder',
  meta: [
    {
      charset: "utf-8",
    },
    {
      name: "viewport",
      content: "width=device-width, initial-scale=1"
    },
    {
      hid: "description",
      name: "description",
      content: "This is a resume builder"
    },
  ],
})

definePageMeta({
  layout: "template3",
})

</script>

<style scoped></style>