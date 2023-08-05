<template>
   <div class="container">
      <div class="row">
         <div class="col-md-2 text-center">
            <NuxtLink class="prev-link" :to="'/resume/create'">Previous</NuxtLink>
         </div>
         <div class="col-md-8">
            <div>
               <div class="card mb-2">
            <div class="card-body rounded">
                <h4 class="text-center text-uppercase bold">Education</h4>
            </div>
        </div>
        <div class="card mb-2">
         <div class="card-body">
                  <blockquote class="blockquote mb-0">
                     <p>The customer is very important, the customer will be followed by the customer. It was a complete
                        set from before.</p>
                     <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite>
                     </footer>
                  </blockquote>
               </div>
        </div>

            </div>
         </div>
         <div class="col-md-2 text-center">
            <NuxtLink class="next-link" :to="'/about'">Next</NuxtLink>
         </div>
      </div>
   </div>
</template>
 
<script>
export default {
   // ...
};
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
 