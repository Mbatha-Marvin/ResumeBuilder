<template>
  <div class="parentTitle">
    <div class="childtitle Title">
      <div id="title_name">
        <h1>
          <span><strong class="username">{{ user_profile.first_name }} {{ user_profile.last_name }}</strong></span>
        </h1>
      </div>
      <div id="title_description_job">
        <h4>
          <span><strong class="career-highlight">{{ user_profile.work_title_highlight }}</strong></span>
        </h4>
      </div>
      <div class="row">
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-telephone"></i>
          <span><strong class="phone_number">{{ user_profile.phone_number }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-envelope-at"></i>
          <span><strong class="email">{{ user_profile.email }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-linkedin"></i>
          <span><strong class="linkedIn">{{ user_profile.linkein_url }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-link-45deg"></i>
          <span><strong class="personal_website">{{ user_profile.personal_website_url }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-github"></i>
          <span><strong>{{ user_profile.github_url }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-mailbox2"></i>
          <span><strong>{{ user_profile.address }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-geo-alt-fill"></i>
          <span><strong class="address">{{ user_profile.city }} , {{ user_profile.country }}</strong></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  const { user_profile } = defineProps(['user_profile'])
</script>

<style scoped></style>
