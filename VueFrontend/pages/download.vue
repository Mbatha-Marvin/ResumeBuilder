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
import html2canvas from 'html2canvas';

export default {
  methods: {
    async generatePDF() {
      // Get the printable content
      const content = this.$el;

      // Create a new jsPDF instance
      const pdf = new jsPDF();
      
        // Exclude the button element from the canvas
        const clonedContent = content.cloneNode(true);
      const buttonElement = clonedContent.querySelector('button');
      if (buttonElement) {
        buttonElement.style.display = 'none';
      }

      // Convert HTML to canvas
      try {
        const canvas = await html2canvas(content);

        // Add canvas image to the PDF
        const imageData = canvas.toDataURL('image/png');
        pdf.addImage(imageData, 'PNG', 15, 15, 180, 0);

        // Save the PDF
        pdf.save('generated_pdf.pdf');
      } catch (error) {
        console.error('Error generating PDF:', error);
      }
    },
  },
};
</script>

