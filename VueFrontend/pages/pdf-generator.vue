<template>
  <div>
    <!-- Your page content goes here -->
    <h1>Hello, this is the main page content</h1>
    <p>This is some sample text in the main page.</p>

    <!-- Add a button to generate PDF -->
    <button @click="generatePDF">Generate PDF</button>
  </div>
</template>

<script>
import jsPDF from 'jspdf';

export default {
  methods: {
    generatePDF() {
      // Get the content from the "index.vue" template
      const content = this.$options.template;

      // Create a new jsPDF instance
      const pdf = new jsPDF();
      pdf.text(20, 20, content);

      // Save the PDF
      pdf.save('generated_pdf.pdf');
    },
  },
};
</script>
