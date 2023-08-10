<template>
   <div class="container">
      <div class="row">
         <div class="col-md-12">
               <div class="card mb-2">
                  <div class="card-body rounded">
                     <h4 class="text-center text-uppercase bold">Education</h4>
                  </div>
               </div>
               <div class="card mb-2">
                  <div class="card-body">
                     <form class="form form-horizontal">
                        <div class="form-body">
                           <div class="row">
                              <div class="col-md-6">
                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput1">Fist Name</label>
                                    <div class="col-md-9">
                                       <input type="text" id="userinput1" class="form-control border-primary"
                                          placeholder="First Name" name="firstname">
                                    </div>
                                 </div>
                              </div>
                              <div class="col-md-6">
                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput2">Last Name</label>
                                    <div class="col-md-9">
                                       <input type="text" id="userinput2" class="form-control border-primary"
                                          placeholder="Last Name" name="lastname">
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="row">
                              <div class="col-md-6">
                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput3">Username</label>
                                    <div class="col-md-9">
                                       <input type="text" id="userinput3" class="form-control border-primary"
                                          placeholder="Username" name="username">
                                    </div>
                                 </div>
                              </div>
                              <div class="col-md-6">
                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput4">Nick Name</label>
                                    <div class="col-md-9">
                                       <input type="text" id="userinput4" class="form-control border-primary"
                                          placeholder="Nick Name" name="nickname">
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div class="row">
                              <div class="col-md-6">
                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput5">Email</label>
                                    <div class="col-md-9">
                                       <input class="form-control border-primary" type="email" placeholder="email"
                                          id="userinput5">
                                    </div>
                                 </div>

                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput6">Website</label>
                                    <div class="col-md-9">
                                       <input class="form-control border-primary" type="url" placeholder="http://"
                                          id="userinput6">
                                    </div>
                                 </div>

                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control">Contact Number</label>
                                    <div class="col-md-9">
                                       <input class="form-control border-primary" type="tel" placeholder="Contact Number"
                                          id="userinput7">
                                    </div>
                                 </div>
                              </div>
                              <div class="col-md-6">
                                 <div class="form-group row mb-2">
                                    <label class="col-md-3 label-control" for="userinput8">Bio</label>
                                    <div class="col-md-9">
                                       <textarea id="userinput8" rows="6" class="form-control border-primary" name="bio"
                                          placeholder="Bio"></textarea>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>

                        <div class="form-actions right">
                           <button type="button" class="btn btn-danger mr-2">
                              <i class="bi bi-x-lg"></i> Cancel
                           </button>
                           <button type="submit" class="btn btn-primary">
                              <i class="bi bi-check2-square"></i> Save
                           </button>
                        </div>
                     </form>
                  </div>
               </div>

            </div>
         </div>

      </div>

</template>
 
<script setup>
definePageMeta({
   layout: "sidestar",
})
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
}</style>
 