<template>
    <!-- https://cdn.pixabay.com/photo/2020/10/27/06/37/man-5689701_1280.jpg -->
    <div class="container">
      <div class="card border border-light">
        <div class="card-body">
          <div class="card border-light shadow text-center mb-2">
            <h1>Services</h1>
            <div class="card-body">
              <blockquote class="blockquote mb-0">
                <p>Unlock jobs with brilliant and professional resume!</p>
                <footer class="blockquote-footer">Create By Profile</footer>
              </blockquote>
            </div>
          </div>
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