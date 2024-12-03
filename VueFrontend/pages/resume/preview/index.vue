<template>
  <div class="container mt-5">
    <!-- PDF Content wrapped in a div for the layout -->
    <div ref="pdfContent" class="pdf-content">
      <div v-for="(user, index) in users" :key="index">
        <!-- Resume Title - Full width, centered -->
        <div class="title-section">
          <ResumeTemp3Title :user_profile="user.user_profile" />
        </div>

        <!-- Two-column layout for sections -->
        <div class="resume-columns">
          <!-- Left Column -->
          <div class="left-column">
            <ResumeTemp3Summary :summary="user.summary" />
            <ResumeTemp3Experience :experience="user.experience" />
            <ResumeTemp3Skills :skills="user.skills" />
            <ResumeTemp3Objective :objective="user.objectives" />
            <ResumeTemp3Frameworks />
            <ResumeTemp3Programming />
            <ResumeTemp3Projects :projects="user.project" />
          </div>

          <!-- Right Column -->
          <div class="right-column">
            <ResumeTemp3Education :education="user.education" />
            <ResumeTemp3Certification :certification="user.certification" />
            <ResumeTemp3Languages :languages="user.language" />
            <ResumeTemp3Operating_Systems />
            <ResumeTemp3Hobbies :hobbies="user.hobbies" />
            <ResumeTemp3Referees :referee="user.referee" />
          </div>
        </div>
      </div>

<!-- Hidden Download Button (visible only during PDF generation) -->
<div class="d-grid gap-2 col-6 mx-auto mb-3 hide-for-print">
        <button @click="generatePDF" :disabled="isGenerating" class="btn btn-success">
          {{ isGenerating ? 'Generating PDF...' : 'Download PDF' }}
        </button>
      </div>

    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axiosT from 'axios';
import ResumeTemp3Title from '~/components/ResumeTemp3/Title.vue';
import ResumeTemp3Summary from '~/components/ResumeTemp3/Summary.vue';
import ResumeTemp3Education from '~/components/ResumeTemp3/Education.vue';
import ResumeTemp3Experience from '~/components/ResumeTemp3/Experience.vue';
import ResumeTemp3Skills from '~/components/ResumeTemp3/Skills.vue';
import ResumeTemp3Objective from '~/components/ResumeTemp3/Objective.vue';
import ResumeTemp3Certification from '~/components/ResumeTemp3/Certification.vue';
import ResumeTemp3Frameworks from '~/components/ResumeTemp3/Frameworks.vue';
import ResumeTemp3Programming from '~/components/ResumeTemp3/Programming.vue';
import ResumeTemp3Languages from '~/components/ResumeTemp3/Languages.vue';
import ResumeTemp3Operating_Systems from '~/components/ResumeTemp3/Operating_Systems.vue';
import ResumeTemp3Hobbies from '~/components/ResumeTemp3/Hobbies.vue';
import ResumeTemp3Projects from '~/components/ResumeTemp3/Projects.vue';
import ResumeTemp3Referees from '~/components/ResumeTemp3/Referees.vue';

interface UserProfile {
  user_profile: string;
  summary: string;
  education: string;
  experience: string;
  skills: string;
  objectives: string;
  certification: string;
  language: string;
  hobbies: string;
  project: string;
  referee: string;
}

const users = ref<UserProfile[]>([]);
const pdfContent = ref<HTMLElement | null>(null);
const user_id = 1;
const axios = useNuxtApp().$axios;
const isGenerating = ref(false);


definePageMeta({
  layout: 'sidestar',
});

useHead({
  title: "Resume Preview",
  meta: [
    { name: "description", content: "View a detailed resume preview with sections like education, experience, skills, and more." },
    { property: "og:title", content: "Resume Preview" },
    { property: "og:description", content: "View a detailed resume preview with various sections." },
    { property: "og:type", content: "website" },
    { property: "og:image", content: "URL-to-image.jpg" },
    { name: "twitter:card", content: "summary_large_image" },
    { name: "twitter:title", content: "Resume Preview" },
    { name: "twitter:description", content: "View a detailed resume preview with sections like education, experience, skills, and more." },
  ],
});

const generatePDF = async (): Promise<void> => {
  if (pdfContent.value) {
    const content = pdfContent.value.innerHTML;
    isGenerating.value = true; 

    try {
      const response = await axiosT.post('/api/generate-pdf', {
        html: content,
      }, {
        responseType: 'blob',
      });

      const blobUrl = URL.createObjectURL(response.data);
      const link = document.createElement('a');
      link.href = blobUrl;
      link.download = 'generated-pdf.pdf';
      link.click();

      URL.revokeObjectURL(blobUrl);
    } catch (error) {
      console.error('Error generating PDF:', error);
    } finally{
      isGenerating.value = false; 
    }
  }
};

const fetchData = async (): Promise<void> => {
  try {
    const { data } = await axios.get(`/user/${user_id}/full_profile`);
    console.log(data);
    
    users.value = [data];
  } catch (error) {
    console.error('Error fetching users:', error);
  }
};

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
/* A4 Page Layout for PDF */
.pdf-content {
  max-width: 210mm; /* A4 Page width */
  margin: 0 auto;
  padding: 10mm;
  box-sizing: border-box;
  page-break-before: always;
}

/* Two-column Layout for sections */
.resume-columns {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

.left-column,
.right-column {
  width: 48%;
  box-sizing: border-box;
}

/* Hide the button in UI but show it during PDF generation */
.hide-for-print {
  display: block;
}

@media print {
  .hide-for-print {
    display: none; /* Hide the button when printing */
  }

  /* PDF content layout adjustments */
  .pdf-content {
    padding: 10mm;
    page-break-before: always;
  }
}

/* Styling for the Resume Sections */
.resume-section {
  margin-bottom: 20px;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.btn-success {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}

.btn-success:hover {
  background-color: #218838;
}
</style>
