<template>
  <div class="template3" v-for="(user, index) in users" :key="index">
    <ResumeTemp3.Title :resume="user" />
    <div class="parent">
      <ResumeTemp3.Summary :resume="user"/>
      <ResumeTemp3.Experience :experience="user.experience_details" />
      <ResumeTemp3.Education :education="user.education_details" />
      <ResumeTemp3.Skills />
      <ResumeTemp3.Objective />
      <ResumeTemp3.Certification />
      <ResumeTemp3.Frameworks />
      <ResumeTemp3.Programming />
      <ResumeTemp3.Languages :languages="user.language_details" />
      <ResumeTemp3.Operating_Systems />
      <ResumeTemp3.Hobbies />
      <ResumeTemp3.Personal_Projects :projects="user.project_details" />
      <ResumeTemp3.Reference />
    </div>
    <div class="d-grid gap-2 col-6 mx-auto mb-3">
        <button class="btn btn-success">Download PDF</button>
      </div>
  </div>
</template>

<script >
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'fetchData',
  setup() {
    const users = ref([]);

    const fetchData = async () => {
      try {
        const response = await useFetch('http://localhost:5000/users/1/profile');
        if (response.status.value == "success") {
          const usersData = response.data.value;
          users.value = [usersData];
          console.log(response);
        } else {
          console.log(response);
        }
      } catch (error) {
        console.error('Error fetching users:', error);
        users.value = [];
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      users,
    };
  },
});
</script>
