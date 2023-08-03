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

<script>
import jsPDF from 'jspdf';

export default {
  methods: {
    generatePDF() {
      // Get the content from the "index.vue" template
      const content = this.$el;

      // Create a new jsPDF instance
      const pdf = new jsPDF();
      pdf.text(20, 20, content);

      // Save the PDF
      pdf.save('generated_pdf.pdf');
    },
  },
};
</script>
