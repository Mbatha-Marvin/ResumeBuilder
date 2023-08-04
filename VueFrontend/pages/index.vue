<template>
  <!-- https://cdn.pixabay.com/photo/2020/10/27/06/37/man-5689701_1280.jpg -->
  <div class="container">
    <div class="card border border-light">
      <div class="card-body">
        <div class="card border-light  text-center mb-2">
          <h1>Welcome to Resume Builder</h1>
          <div class="card-body">
            <blockquote class="blockquote mb-0">
              <p>Unlock jobs with brilliant and professional resume!</p>
              <footer class="blockquote-footer">Find more</footer>
            </blockquote>
          </div>
        </div>

        <div class="card border-light shadow text-center mb-2">
          <div class="card-body">
            <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://cdn.pixabay.com/photo/2018/06/02/22/58/career-3449422_1280.png" class="d-block w-100"
                    alt="...">
                </div>
                <div class="carousel-item">
                  <img src="https://cdn.pixabay.com/photo/2018/09/16/10/16/job-3681036_640.jpg" class="d-block w-100"
                    alt="...">
                </div>
                <div class="carousel-item">
                  <img src="https://cdn.pixabay.com/photo/2021/09/15/15/49/resume-6627200_640.jpg" class="d-block w-100"
                    alt="...">
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="card border-light shadow text-center mb-2">
          <h1>Services</h1>
          <div class="card-body">
            <blockquote class="blockquote mb-0">
              <p>Unlock jobs with brilliant and professional resume!</p>
              <footer class="blockquote-footer">Find more</footer>
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