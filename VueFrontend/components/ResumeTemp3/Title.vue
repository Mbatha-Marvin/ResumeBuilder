<template>
  <div class="parentTitle">
    <div class="childtitle Title">
      <div id="title_name">
        <h1>
          <span><strong>Ronald Kimeli</strong></span>
        </h1>
      </div>
      <div id="title_description_job">
        <h4>
          <span><strong>Web Developer | database Designer | Fullstack Developer</strong></span>
        </h4>
      </div>
      <div class="row">
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-telephone"></i>
          <span><strong>254 798 298834</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-envelope-at"></i>
          <span><strong>kimeliryans@gmail.com</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-linkedin"></i>
          <span><strong>https://www.linkedin.com/in/ronald-kimeli</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-link-45deg"></i>
          <span><strong>leave-managent-system.great-site.net</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-github"></i>
          <span><strong>https://github.com/KimelirR</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-geo-alt-fill"></i>
          <span><strong>Moi Avenue, Nairobi, Kenya</strong></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

const { data: products } = await useFetch('https://fakestoreapi.com/products')
console.log(typeof(products));

</script>

<style scoped></style>
