<template>
    <div class="child work-experience">
      <div class="mb-2" id="section-title">
        <h4><strong>Work Experience</strong></h4>
      </div>

      <div id="experience-title">
        <h5><strong>Full Stack Web developer </strong></h5>
      </div>
      <div class="company-title">
        <img class="masterclass"
          src="https://media.licdn.com/dms/image/C4E0BAQE_7aTYL3mx3A/company-logo_100_100/0/1519876031194?e=1696464000&v=beta&t=2zKpDQnJPm-KoC0bDtWQHe3DMPTkiZ6hVau82YDr2to"
          alt="logo" />Masterclass Solutions
      </div>

      <div class="iconic-section">
        <i class="bi bi-link-45deg mr-2"></i>
        https://leave-managent-system.great-site.net
      </div>
      <div class="iconic-section">
        <span><i class="bi bi-geo-alt-fill"></i></span>
        <strong>Nairobi, Kenya</strong>
      </div>
      <div class="row">
        <div class="col-md-6 iconic-section">
          Start Date: <strong>02/12/2020</strong>
        </div>
        <div class="col-md-6 iconic-section">
          End Date: <strong>Present</strong>
        </div>
      </div>

      <div>
        <h6><b>Achievements</b></h6>
      </div>
      <ul>
        <li>Integrated Application tracking system API</li>
        <li>Improved and optimized Database design for givecloud client</li>
        <li>Developed locations API using Laravel</li>
        <li>Upgraded a PHP website</li>
        <li>Created a news aggreggator website</li>
      </ul>
    </div>
</template>

<script setup>

</script>

<style scoped>
#section-title {
    border-bottom: 2px solid #080808 !important;
}

.experience {
    text-align: left !important;
}

#experience-title {
    text-align: start !important;
    text-decoration: none !important;
    width: auto !important;
}

.iconic-section {
    text-align: start !important;
    padding: auto !important;
    width: auto !important;
}

img {
    background-color: inherit !important;
    height: 20px !important;
    width: 20px !important;
    margin-right: 4px !important;
}

.company-title {
    background-color: inherit !important;
    size: 20px !important;
}
</style>