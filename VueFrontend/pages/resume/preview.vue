<!-- <template>
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
      <button @click="generatePDFL" class="btn btn-success">Download PDF</button>
    </div>
  </div>
</template> -->

<!-- <script >
import { defineComponent, ref, onMounted } from 'vue';
import axiosT from 'axios';
import jsPDF from 'jspdf';

definePageMeta({
  layout: "sidestar",
})


export default defineComponent({
  name: 'fetchData',
  setup() {
    const users = ref([]);
    const pdfContent = ref(null);
    const user_id = 1;
    const axios = useNuxtApp().$axios;

    const generatePDFL = async() => {
      const content = pdfContent.value;
     
      const pdf = new jsPDF();
      pdf.text(20, 20, content[0]);

      // Save the PDF
      pdf.save('generated_pdf.pdf');
    };

    const generatePDF = async () => {

      const content = pdfContent.value;

      try {
        const response = await axiosT.post('http://localhost:3000/generate-pdf', {
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
      generatePDF,
      generatePDFL
    };
  },
});
</script> -->


<!-- <script>
import { defineComponent, ref, onMounted } from 'vue';
import axiosT from 'axios';

export default defineComponent({
name: 'fetchData',
setup() {
const users = ref([]);
const pdfContent = ref(null);
const user_id = 1;
const axios = useNuxtApp().$axios;

const generatePDFL = async () => {
  if (process.client) {  // Ensure this runs only on the client side
    const html2pdf = (await import('html2pdf.js')).default;

    const content = pdfContent.value;

    if (content) {
      const options = {
        margin: [0.5, 0.5, 0.5, 0.5],
        filename: 'generated_pdf.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
      };

      html2pdf().from(content).set(options).save().catch(error => {
        console.error('PDF generation error:', error);
      });
    } else {
      console.error('Content is not available for PDF generation');
    }
  }
};

const fetchData = async () => {
  await axios({
    method: 'get',
    url: `/user/${user_id}/full_profile`,
    headers: { 'Content-Type': 'application/json' },
  })
  .then(response => {
    const usersData = [response.data];
    users.value = usersData;
    console.log(usersData);
  })
  .catch(error => {
    console.error('Error fetching users:', error);
  });
};

onMounted(() => {
  fetchData();
});

return {
  users,
  pdfContent,
  generatePDFL
};
},
});
</script> -->

<!-- <template>
  <div>
    <div id="content">
      <h1>Test PDF</h1>
      <p>This is a test PDF content.</p>
    </div>
    <button @click="generatePDFL">Download PDF</button>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'SimpleTest',
  setup() {
    const generatePDFL = async () => {
      if (process.client) { // Ensure this code runs only on the client side
        // Dynamically import html2pdf.js
        const { default: html2pdf } = await import('html2pdf.js');
        
        // Get the content element
        const content = document.getElementById('content');
        console.log(content);
        return;
        
        if (content) {
          const options = {
            margin: [0.5, 0.5, 0.5, 0.5],
            filename: 'test.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
          };

          html2pdf().from(content).set(options).save().catch(error => {
            console.error('PDF generation error:', error);
          });
        } else {
          console.error('Content element not found');
        }
      } else {
        console.error('Code is not running on the client side');
      }
    };

    return {
      generatePDFL
    };
  }
});
</script> -->


<!-- <template>
  <div>
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
    </div>
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
      <button @click="generatePDF" class="btn btn-success">Download PDF</button>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useNuxtApp } from '#app';

export default defineComponent({
  name: 'fetchData',
  setup() {
    const users = ref([]);
    const pdfContent = ref(null);
    const user_id = 1;
    const axios = useNuxtApp().$axios;

    const generatePDF = async () => {
      if (process.client) { 
        // Dynamically import html2pdf.js
        const { default: html2pdf } = await import('html2pdf.js');
        
        // Get the content element
        const content = pdfContent.value[0];
            
        if (content) {
          const options = {
            margin: [0.5, 0.5, 0.5, 0.5],
            filename: 'test.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
          };

          html2pdf().from(content).set(options).save().catch(error => {
            console.error('PDF generation error:', error);
          });
        } else {
          console.error('Content element not found');
        }
      } else {
        console.error('Code is not running on the client side');
      }
    };

    const fetchData = async () => {
      try {
        const response = await axios.get(`/user/${user_id}/full_profile`, {
          headers: { 'Content-Type': 'application/json' }
        });
        users.value = [response.data];
        // console.log(users.value);
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      users,
      pdfContent,
      generatePDF
    };
  }
});
</script>  -->



<!-- <template>
  <div>
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
    </div>
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
      <button @click="generatePDF" class="btn btn-success" :disabled="isDownloading">
        {{ isDownloading ? 'Downloading...' : 'Download PDF' }}
      </button>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useNuxtApp } from '#app';

export default defineComponent({
  name: 'fetchData',
  setup() {
    const users = ref([]);
    const pdfContent = ref(null);
    const isDownloading = ref(false);

    const generatePDF = async () => {
      if (process.client) {
        isDownloading.value = true;
        try {
          const { default: html2pdf } = await import('html2pdf.js');
          const content = pdfContent.value[0];
              
          if (content) {
            const options = {
              margin: [0.5, 0.5, 0.5, 0.5],
              filename: 'resume.pdf',
              image: { type: 'jpeg', quality: 0.98 },
              html2canvas: { scale: 2, logging: true }, // Enable logging for debugging
              jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };

            await html2pdf().from(content).set(options).save();
          } else {
            console.error('Content element not found');
          }
        } catch (error) {
          console.error('PDF generation error:', error);
        } finally {
          isDownloading.value = false;
        }
      } else {
        console.error('Code is not running on the client side');
      }
    };

    const fetchData = async () => {
      try {
        const response = await useNuxtApp().$axios.get(`/user/1/full_profile`, {
          headers: { 'Content-Type': 'application/json' }
        });
        users.value = [response.data];
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      users,
      pdfContent,
      generatePDF,
      isDownloading
    };
  }
});
</script> -->


<!-- <template>
  <div>
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
    </div>
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
      <button @click="generatePDF" class="btn btn-success" :disabled="isDownloading">
        {{ isDownloading ? 'Downloading...' : 'Download PDF' }}
      </button>
    </div>
  </div>
</template> -->

<template>
  <div>

    <div class="d-flex justify-content-center mb-2">
      <i class="bi bi-file-earmark-pdf export-icon" @click="generatePDF" :class="{ 'disabled': isDownloading }"></i>
    </div>


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
    </div>
  </div>
</template>


<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useNuxtApp } from '#app';

export default defineComponent({
  name: 'fetchData',
  setup() {
    // Define reactive properties
    const users = ref([]);
    const pdfContent = ref(null);
    const isDownloading = ref(false);

    // Set meta information
    useHead({
      title: 'Resume Preview - Export PDF',
      meta: [
        { name: 'description', content: 'Generate and export a PDF of the user profile with ease. Click the icon to download the resume in PDF format.' },
        { property: 'og:title', content: 'Resume Preview - Export PDF' },
        { property: 'og:description', content: 'Generate and export a PDF of the user profile with ease. Click the icon to download the resume in PDF format.' }
      ]
    });

    // Method to generate PDF
    const generatePDF = async () => {
      if (process.client) {
        isDownloading.value = true;
        try {
          // Dynamically import html2pdf.js
          const { default: html2pdf } = await import('html2pdf.js');
          const content = pdfContent.value[0];

          if (content) {
            const options = {
              margin: [0.5, 0.5, 0.5, 0.5],
              filename: 'resume.pdf',
              image: { type: 'jpeg', quality: 0.98 },
              html2canvas: { scale: 2 },
              jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
              // jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' } // Set format to A4
            };

            await html2pdf().from(content).set(options).save();
          } else {
            console.error('Content element not found');
          }
        } catch (error) {
          console.error('PDF generation error:', error);
        } finally {
          isDownloading.value = false;
        }
      } else {
        console.error('Code is not running on the client side');
      }
    };

    // Fetch user data
    const fetchData = async () => {
      try {
        const response = await useNuxtApp().$axios.get(`/user/1/full_profile`, {
          headers: { 'Content-Type': 'application/json' }
        });
        users.value = [response.data];
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      users,
      pdfContent,
      generatePDF,
      isDownloading
    };
  }
});
</script>

<style>
.template3 {
  user-select: text;
}

.export-icon {
  font-size: 36px;
  /* Adjust size as needed */
  color: #28a745;
  /* Bootstrap success color */
  cursor: pointer;
  transition: color 0.3s;
}

.export-icon:hover {
  color: #218838;
  /* Darker shade on hover */
}

.export-icon.disabled {
  color: #6c757d;
  /* Bootstrap muted color for disabled state */
  cursor: not-allowed;
}

.d-flex {
  display: flex;
}

.justify-content-center {
  justify-content: center;
}

.mb-2 {
  margin-bottom: 0.5rem !important;
  /* Reduced bottom margin */
}
</style>
