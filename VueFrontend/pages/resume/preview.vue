<template>
   <div class="container">
     <div class="template3">
       <ResumeTemp4.Title />
       <div class="parent">
         <ResumeTemp4.Summary />
         <ResumeTemp4.Skills />
         <ResumeTemp4.Experience />
         <ResumeTemp4.Education />
         <ResumeTemp4.Certification />
         <ResumeTemp4.Frameworks />
         <ResumeTemp4.Programming />
         <ResumeTemp4.Languages />
         <ResumeTemp4.OperatingSystems />
         <ResumeTemp4.Hobbies />
         <ResumeTemp4.Personal_Projects />
         <ResumeTemp4.Reference />
       </div>
       <div class="d-grid gap-2 col-6 mx-auto mb-3">
         <button ref="pdfButton" @click="generatePDF" class="btn btn-success">Download PDF</button>
       </div>
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