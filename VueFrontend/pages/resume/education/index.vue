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
                           <NuxtLink :to="'/resume/education/create'" class="btn btn-sm btn-success float-end"><i
                                 class="bi bi-plus-lg"></i>Add
                           </NuxtLink>
                        </p>
                     </div>
                     <div v-for="(item, index) in educations" :key="index" class="card mt-2">
                        <div class="card-body">
                           <form class="form form-horizontal">
                              <div class="form-body">
                                 <div class="row">
                                    <div class="col-md-12">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-6 label-control" for="userinput1">Course Title</label>
                                          <div class="col-md-6">
                                             <div>{{item.course_title}}</div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <div class="row">
                                    <div class="col-md-6">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-3 label-control" for="course_title">School Name</label>
                                          <div class="col-md-9">
                                             <div>{{item.course_title}}</div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-md-6">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-3 label-control" for="location">Location</label>
                                          <div class="col-md-9">
                                             <div>{{item.location}}</div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <div class="row">
                                    <div class="col-md-6">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-3 label-control" for="education_level">Education Level</label>
                                          <div class="col-md-9">
                                             <div>{{item.education_level}}</div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-md-6">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-3 label-control" for="final_grade">Final Grade</label>
                                          <div class="col-md-9">
                                             <div>{{item.final_grade}}</div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <div class="row">
                                    <div class="col-md-6">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-3 label-control" for="start_date">Start Date</label>
                                          <div class="col-md-9">
                                             <div>{{item.start_date}}</div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-md-6">
                                       <div class="form-group row mb-2">
                                          <label class="col-md-3 label-control">End date</label>
                                          <div class="col-md-9">
                                             <div>{{item.end_date}}</div>
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
  
<script>
import { defineComponent, ref, onMounted } from 'vue';
definePageMeta({
         layout: "sidestar",
      });
export default defineComponent({
   name: 'EducationList',
   setup() {



      const educations = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });
      const axios = useNuxtApp().$axios;
      const user_id = 1;

      const getEducation = async () => {
         await axios({
            method: 'get',
            url: `/user/${user_id}/eduaction/`,
            headers: { 'Content-Type': 'application/json' },
         })
            .then(function (response) {
               educations.value = response.data;
               console.log(response);
            })
            .catch(function (error) {
               console.error('Error fetching educations:', error);
            });
      };

      const deleteEducation = async (user_id) => {
         await axios({
                    method: 'delete',
                    url: `/user/${user_id}/eduaction/`,
                    headers: { 'Content-Type': 'application/json' },
                })
                    .then(function (response) {
                      getEducation();
                     console.log(response);
                    })
                    .catch(function (error) {
                     console.error('Error deleting user:', error);
                    });

      };

      onMounted(() => {
         getEducation();
      });

      return {
         educations,
         deleteEducation,
      };
   },
});
</script>
  
<style></style>
  