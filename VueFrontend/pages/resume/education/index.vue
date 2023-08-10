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
                <div class="card-content collapse show">
                   <div class="card-body card-dashboard">
                      <div class="row">
                         <p class="d-inline">To Update use update button
                            <NuxtLink :to="'/resume/education/create'" class="btn btn-sm btn-success float-end"><i class="bi bi-plus-lg"></i>Add
                            </NuxtLink>
                         </p>
                      </div>
                      <div class="card">
                         <div class="card-body">
                            <form class="form form-horizontal">
                               <div class="form-body">
                                  <div class="row">
                                     <div class="col-md-12">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-6 label-control" for="userinput1">Course Title</label>
                                           <div class="col-md-6">
                                              <div>John</div>
                                           </div>
                                        </div>
                                     </div>
                                  </div>
                                  <div class="row">
                                     <div class="col-md-6">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-3 label-control" for="userinput3">School Name</label>
                                           <div class="col-md-9">
                                              <div>John</div>
                                           </div>
                                        </div>
                                     </div>
                                     <div class="col-md-6">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-3 label-control" for="userinput4">Location</label>
                                           <div class="col-md-9">
                                              <div>John</div>
                                           </div>
                                        </div>
                                     </div>
                                  </div>
                                  <div class="row">
                                     <div class="col-md-6">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-3 label-control" for="userinput2">Education Level</label>
                                           <div class="col-md-9">
                                              <div>Deer</div>
                                           </div>
                                        </div>
                                     </div>
                                     <div class="col-md-6">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-3 label-control" for="userinput5">Final Grade</label>
                                           <div class="col-md-9">
                                              <div>John</div>
                                           </div>
                                        </div>
                                     </div>
                                  </div>
                                  <div class="row">
                                     <div class="col-md-6">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-3 label-control" for="userinput6">Start Date</label>
                                           <div class="col-md-9">
                                              <div>John</div>
                                           </div>
                                        </div>
                                     </div>
                                     <div class="col-md-6">
                                        <div class="form-group row mb-2">
                                           <label class="col-md-3 label-control">End date</label>
                                           <div class="col-md-9">
                                              <div>John</div>
                                           </div>
                                        </div>
                                     </div>
                                  </div>
                               </div>
                            </form>
                         </div>
                      </div>
                   </div>
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
 }
 </style>
  