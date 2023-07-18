<template>
  <!-- <div class="template1">
    <ResumeTemp1.Title />
    <br />
    <div class="row col-md-12 ml-2 mr-2">
      <ResumeTemp1.Summary />
      <ResumeTemp1.Languages />
      <ResumeTemp1.Experience />
      <ResumeTemp1.Skills />
      <ResumeTemp1.Programming />
      <ResumeTemp1.Education />
      <ResumeTemp1.Certification />
      <ResumeTemp1.Hobbies />
      <ResumeTemp1.Personal_Projects />
      <ResumeTemp1.Reference />
    </div>
    
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
      <button ref="pdfButton" @click="generatePDF" class="btn btn-success">Download PDF</button>
    </div>
  </div> -->


  <!-- <button ref="pdfButton" @click="generatePDF" class="btn btn-danger float-end mb-2">Generate PDF</button>
    <ResumeTemp2.Title />
    <div class="parent">
      <ResumeTemp2.Summary />
      <ResumeTemp2.Languages />
      <ResumeTemp2.Experience />
      <ResumeTemp2.Skills />
      <ResumeTemp2.Programming />
      <ResumeTemp2.Education />
      <ResumeTemp2.Certification />
      <ResumeTemp2.Hobbies />
      <ResumeTemp2.Personal_Projects />
      <ResumeTemp2.Reference />
    </div> -->
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


  <header>
    <nav>
      <ul>
        <li>
          <NuxtLink to="/about">About</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/posts">Posts</NuxtLink>
        </li>
      </ul>
    </nav>
  </header>
  <div>
    allow me to take such chance
  </div>
  <Footer />
</template>
  
  
<script setup>
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
  