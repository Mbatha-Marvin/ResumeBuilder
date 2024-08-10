<template>
    <div class="row py-4 px-2">
      <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
               <div class="card-body rounded">
                  <h4 class="text-center text-uppercase bold">Let's start!</h4>
               </div>
            </div>
            <div class="card mb-2">
               <div class="card-body">
                  <blockquote class="blockquote mb-0">
                     <p>Please! Make sure that you complete follow steps before you preview and download your resume
                        Once your profile is complete edit, add sections, preview resume and download resume.</p>
                     <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite>
                     </footer>
                  </blockquote>
               </div>
            </div>

         <div class="text-center">
         <NuxtLink class="next-link float-start" :to="'/resume/profile'">Next</NuxtLink>
      </div>
   </div>
   </div>
</template>
 
<script setup>
        definePageMeta({
            layout: "sidestar",
        });

        // Set meta information
        useHead({
            title: 'Start',
            meta: [
                { name: 'description', content: 'View Start' },
                { property: 'og:title', content: 'Start' },
                { property: 'og:description', content: 'View Start.' }
            ]
        });
</script>
 
<style>
.col-md-2,
.col-md-8 {
   display: flex;
   justify-content: center;
   align-items: center;
}

/* For desktop view */
.prev-link,
.next-link {
   display: inline-block;
   padding: 8px 16px;
   background-color: green;
   border: 2px solid green;
   color: white;
   text-decoration: none;
   border-radius: 10px;
   transition: background-color 0.3s, border-color 0.3s;
}

.prev-link:hover,
.next-link:hover {
   background-color: purple;
   border-color: gold;
   border-radius: 10px;
}

/* For mobile view */
@media (max-width: 767.98px) {

   .col-md-2,
   .col-md-8 {
      display: block;
   }

   .prev-link,
   .next-link {
      display: block;
      margin: 10px auto;
      text-align: center;
   }

   .prev-link {
      order: -1;
   }
}
</style>
 