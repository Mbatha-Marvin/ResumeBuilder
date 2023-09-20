<template>
  <div ref="pdfContent" class="template3" v-for="(user, index) in users" :key="index">
    <ResumeTemp3.Title :user_profile="user.user_profile" />
    <div class="parent">
      <ResumeTemp3.Summary :summary="user.summary" />
      <ResumeTemp3.Education :education="user.education" />
      <ResumeTemp3.Experience :experience="user.experience" />
      <ResumeTemp3.Skills :skills="user.skills" />
      <ResumeTemp3.Objective :objective="user.objectives" />
      <ResumeTemp3.Certification :certification="user.certification" />
      <ResumeTemp3.Frameworks />
      <ResumeTemp3.Programming />
      <ResumeTemp3.Languages :languages="user.language" />
      <ResumeTemp3.Operating_Systems />
      <ResumeTemp3.Hobbies :hobbies="user.hobbies" />
      <ResumeTemp3.Projects :projects="user.project" />
      <ResumeTemp3.Referees :referee="user.referee" />
    </div>
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
      <button @click="generatePDF" class="btn btn-success">Download PDF</button>
    </div>
  </div>
</template>

<script >
import { defineComponent, ref, onMounted } from 'vue';
import axiosT from 'axios';

definePageMeta({
  layout: "template3",
})


export default defineComponent({
  name: 'fetchData',
  setup() {
    const users = ref([]);
    const template3 = ref('');
    const pdfContent = ref('');
    const user_id = 1;
    const axios = useNuxtApp().$axios;

    const generatePDF = async () => {
      
      const content = pdfContent.value;

      try {
        const response = await axiosT.post('http://localhost:3000/generate-pdf', {
          html: content.innerHTML,
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
        console.error('PDF generation error:', error);
      }
    }

    const fetchData = async () => {

      await axios({
        method: 'get',
        url: `/user/${user_id}/full_profile`,
        headers: { 'Content-Type': 'application/json' },
      })
        .then(function (response) {
          const usersData = [response.data];
          users.value = usersData;
          console.log(usersData);
        })
        .catch(function (error) {
          console.error('Error fetching users:', error);
          // users.value = [];
        });
    };

    onMounted(() => {
      fetchData();
    });

    return {
      users,
      pdfContent,
      generatePDF
    };
  },
});
</script>
