<template>
  <div class="template3">
    <ResumeTemp3.Title />
    <div class="parent">
      <ResumeTemp3.Summary />
      <ResumeTemp3.Languages />
      <ResumeTemp3.Experience />
      <ResumeTemp3.Programming />
      <ResumeTemp3.Skills />
      <ResumeTemp3.Education />
      <ResumeTemp3.Certification />
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
         const pdf = new jsPDF();
   
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
         } finally {
           // Restore the button's display property
           this.$refs.pdfButton.style.display = '';
         }
       },
     },
   };
   
   const appConfig = useHead({
     title: 'ResumeBuilder',
     theme: {
       dark: true,
       colors: {
         primary: '#ff0000'
       }
     },
   });
   
   definePageMeta({
     layout: "template3",
   })
   
   </script>
   
   <style scoped></style>