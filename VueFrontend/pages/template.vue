<template>
  <div class="template3" v-if="users" v-for="res in users" key="res.name">
    <ResumeTemp3.Title :resume="res" />
    <div class="parent">
      <ResumeTemp3.Summary />
      <ResumeTemp3.Skills />
      <ResumeTemp3.Experience />
      <ResumeTemp3.Education />
      <ResumeTemp3.Certification />
      <ResumeTemp3.Frameworks />
      <ResumeTemp3.Programming />
      <ResumeTemp3.Languages />
      <ResumeTemp3.OperatingSystems />
      <ResumeTemp3.Hobbies />
      <ResumeTemp3.Personal_Projects />
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
          users.value = usersData;
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
