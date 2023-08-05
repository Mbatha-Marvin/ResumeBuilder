<template>
    <div>
        <h1>Educationala valuseedd</h1>
      <div v-for="(item, index) in enrollmentData" :key="index" class="enrolment">
        <div class="iconic-section">
          <span>Level : <strong>{{ item.level }}</strong></span>
        </div>
        <div class="iconic-section">
          <span>Proficiency : <strong>{{ item.proficiency }}</strong></span>
        </div>
        <div class="iconic-section">
          <span>Institution : <strong>{{ item.institution }}</strong></span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        enrollmentData: [
          {
            level: 'Bachelors Degree (Bsc)',
            proficiency: 'Computer Science',
            institution: 'University of Kabianga'
          },
          // Add more data objects as needed
        ]
      };
    }
  };
  </script>
  