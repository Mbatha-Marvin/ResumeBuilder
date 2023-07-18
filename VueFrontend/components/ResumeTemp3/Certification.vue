<template>
 <div class="child certification">
      <div id="section-title">
        <h4><strong>Certification</strong></h4>
        <hr class="border border-black border-2 opacity-75">
      </div>
      <div class="certified">
        <div class="iconic-section">
          <span>Certified On : <strong>Data analysis</strong></span>
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
      <div class="certified">
        <div class="iconic-section">
          <span>Certified On : <strong>Data analysis</strong></span>
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
.certification {
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