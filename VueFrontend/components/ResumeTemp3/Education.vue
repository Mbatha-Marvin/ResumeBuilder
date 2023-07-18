<template>
  <div class="child education">
      <div id="section-title">
        <h4><strong>Education</strong></h4>
        <hr class="border border-black border-2 opacity-75">
      </div>
      <div class="enrolment">
        <div class="iconic-section">
          <span>Level : <strong>Bachelors degree (Bsc)</strong></span>
        </div>
        <div class="iconic-section">
          <span>Proficiency : <strong>Computer Science</strong></span>
        </div>
        <div class="iconic-section">
          <span>Institution : <strong>University of Kabianga</strong></span>
        </div>
        <div class="row">
          <div class="col-md-6 iconic-section">
            <span>Start Date : <strong>02/12/2020</strong></span>
          </div>
          <div class="col-md-6 iconic-section">
            <span>End Date : <strong>02/12/2020</strong></span>
          </div>
        </div>
      </div>
      <Helpers.Dotted_hr />
      <div class="enrolment">
        <div class="iconic-section">
          <span>Level : <strong>Bachelors degree (Bsc)</strong></span>
        </div>
        <div class="iconic-section">
          <span>Proficiency : <strong>Computer Science</strong></span>
        </div>
        <div class="iconic-section">
          <span>Institution : <strong>University of Kabianga</strong></span>
        </div>
        <div class="row">
          <div class="col-md-6 iconic-section">
            <span>Start Date : <strong>02/12/2020</strong></span>
          </div>
          <div class="col-md-6 iconic-section">
            <span>End Date : <strong>02/12/2020</strong></span>
          </div>
        </div>
      </div>

    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>


.education {
    text-align: left !important;
}



.parent{
    columns: 2;
    gap: 10px;
    padding: 5px;
    margin: 0 auto;
  }
  
  .child{
    padding: 10px;
    background-color: white;
    display: inline-block;
    width: 100%;  
    margin-bottom: 5px;
  }
</style>