<template>
      <div class="container">
      <div class="card border-light text-center">
        <h1>Welcome to Resume Builder</h1>
        <div class="card-body">
          <blockquote class="blockquote mb-0">
            <p>Unlock jobs with brilliant and professional resume!</p>
            <footer class="blockquote-footer">Find more</footer>
          </blockquote>
        </div>
      </div>
    </div>
</template>

<script >
export default {
  methods: {
     generatePDF() {
          return "generated";
    },
  },
};

useHead({
  title: 'Resume Builder Home',
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
      content: "Welcome to the Resume Builder homepage page"
    },
  ],
})

</script>

<style scoped></style>