<template>
    <div id="title">
        <div class="row col-md-12 ml-2 mr-2">
            <div class="col-md-12" id="title-head">
                <h1><strong>Ronald Kimeli</strong></h1>
            </div>
            <div class="col-md-12" id="title-job">
                <h4>Web Developer | database Designer | Fullstack Developer</h4>
            </div>
            <!-- We will make one of them to be dynamic -->
            <div class="col-md-4 iconic-section">
                <span><i class="bi bi-phone"></i></span> <strong>25798298834</strong>
            </div>
            <div class="col-md-4 iconic-section">
                <span><i class="bi bi-envelope-at"></i></span> <strong>kimeliryans@gmail.com</strong>
            </div>
            <div class="col-md-4 iconic-section">
                <span><i class="bi bi-linkedin"></i></span> <strong>https://www.linkedin.com/in/ronald-kimeli/</strong>
            </div>
            <div class="col-md-4 iconic-section">
                <span><i class="bi bi-link-45deg"></i></span> <strong>leave-managent-system.great-site.net</strong>
            </div>

            <div class="col-md-4 iconic-section">
                <span><i class="bi bi-github"></i></span> <strong>https://github.com/KimelirR</strong>
            </div>

            <div class="col-md-4 iconic-section">
                <span><i class="bi bi-geo-alt-fill"></i></span> <strong>Moi Avenue, Nairobi, Kenya</strong>
            </div>
        </div>
    </div>
    
</template>

<script setup>

</script>

<style scoped>
#title {
    background-color: white !important;
    color: #0a0a0a !important;

}

#title-head,
#title-job {
    text-transform: capitalize;
    text-align: center !important;

}

.iconic-section {
    text-align: start !important;
    padding: auto !important;
    width: auto !important;
}
</style>