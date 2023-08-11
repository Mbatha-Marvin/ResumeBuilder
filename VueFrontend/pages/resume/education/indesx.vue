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
                                 class="bi bi-plus-lg"></i>Create Education
                           </NuxtLink>
                        </p>
                     </div>
                     <div v-for="(newEducation, index) in educations" :key="index" class="card mt-2">
                        <div class="card-content collapse show">
                           <div class="card-body card-dashboard">
                              <div class="row">
                                 <p class="d-inline">
                                 <p class="float-start"><strong>{{ newEducation.education_id }}</strong></p>
                                 <div class="btn-group float-end" role="group" aria-label="Third group">
                                    <button @click="deleteEducation(newEducation.user_id, newEducation.education_id)"
                                       class="btn btn-sm btn-danger mx-2">Delete</button>
                                 </div>
                                 </p>
                              </div>

                              <form @submit.prevent="updateEducation" class="form form-horizontal needs-validation"
                                 novalidate>
                                 <div class="form-body">
                                    <div class="row">
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="course_title">Course
                                                Title</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.course_title" type="text" id="course_title"
                                                   class="form-control border-primary" placeholder="Course Title"
                                                   name="course_title" required>
                                                <span class="invalid-feedback">Course Title is required</span>
                                             </div>
                                          </div>
                                       </div>

                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="card_title">Card
                                                Title</label>
                                             <div class="col-md-9">
                                                <select v-model="newEducation.card_title" class="form-select border-primary"
                                                   aria-label="Default select example" required>
                                                   <option selected :value="newEducation.card_title">{{
                                                      newEducation.card_title }}</option>
                                                   <option>Education</option>
                                                   <option>Academics</option>
                                                </select>
                                                <span class="invalid-feedback">Please Select Card Title</span>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="row">
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="school_name">School
                                                Name</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.school_name" type="text" id="school_name"
                                                   class="form-control border-primary" placeholder="School Name"
                                                   name="school_name" required>
                                                <span class="invalid-feedback">School Name is required</span>
                                             </div>
                                          </div>
                                       </div>
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="location">Location</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.location" type="text" id="location"
                                                   class="form-control border-primary" placeholder="Location"
                                                   name="location" required>
                                                <span class="invalid-feedback">Location is required</span>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="row">
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="education_level">Education
                                                Level</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.education_level" type="text" id="education_level"
                                                   class="form-control border-primary" placeholder="Education Level"
                                                   name="education_level" required>
                                                <span class="invalid-feedback">Education Level is
                                                   required</span>
                                             </div>
                                          </div>
                                       </div>
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="final_grade">Final
                                                Grade</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.final_grade" type="text" id="final_grade"
                                                   class="form-control border-primary" placeholder="Final Grade"
                                                   name="final_grade" required>
                                                <span class="invalid-feedback">Final Grade is required</span>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="row">
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="start_date">Start
                                                Date</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.start_date" type="date" id="start_date"
                                                   class="form-control border-primary" placeholder="Start
                                                            Date" name="start_date" required>
                                                <span class="invalid-feedback">Start
                                                   Date is required</span>
                                             </div>
                                          </div>
                                       </div>
                                       <div class="col-md-6">
                                          <div class="form-group row mb-2">
                                             <label class="col-md-3 label-control" for="end_date">End
                                                date</label>
                                             <div class="col-md-9">
                                                <input v-model="newEducation.end_date" type="date" id="end_date"
                                                   class="form-control border-primary" placeholder="End date"
                                                   name="end_date" required>
                                                <span class="invalid-feedback">End date is required</span>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <div class="form-actions float-center mt-2">
                                    <button type="submit" class="btn btn-primary mx-2">
                                       <i class="bi bi-check2-square"></i> Update
                                    </button>
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
   </div>
</template>
  
<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

definePageMeta({
   layout: "sidestar",
});
export default defineComponent({
   name: 'EducationList',
   setup() {

      const educations = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });
      const newEducation = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });
      
      const axios = useNuxtApp().$axios;
      
      const route = useRoute();
      const router = useRouter();
      
      const user_id = 1;

      const getEducation = async () => {
         await axios({
            method: 'get',
            url: `/user/${user_id}/education/`,
            headers: { 'Content-Type': 'application/json' },
         })
            .then(function (response) {
               educations.value = response.data;
               // console.log(educations.value);
            })
            .catch(function (error) {
               console.error('Error fetching educations:', error);
            });
      };

      
      const updateEducation = async () => {
            const form = document.querySelector('.needs-validation');
            if (form.checkValidity()) {
                await axios({
                     method: 'patch',
                     url: `/user/${user_id}/education/${educations.value[0].education_id}`,
                     headers: { 'Content-Type': 'application/json' },
                     data: JSON.stringify(educations.value),
                  })
                .then(function (response) {
                        // router.push('/resume/education');
                        console.log(response);
                     })
                     .catch(function (error) {
                        console.error(error);
                     });
            } else {
                form.classList.add('was-validated');
            };
        };

      const deleteEducation = async (user_id, education_id) => {
         await axios({
            method: 'delete',
            url: `/user/${user_id}/education/${education_id}`,
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
         
         const forms = document.querySelectorAll('.needs-validation');
         Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
               event.preventDefault();
               event.stopPropagation();

               if (!form.checkValidity()) {
                     form.classList.add('was-validated');
               } else {
                  // getEducation();
                  updateEducation();
               }
            }, false);
         });
      });

      return {
         educations,
         deleteEducation,
         updateEducation
      };
   },
});
</script>
  
<style></style>
  


        <!-- const submitEducationForm = async (educationIndex) => {
            console.log(educationIndex);
            const forms = document.querySelectorAll('.needs-validation');
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    event.preventDefault();
                    event.stopPropagation();

                    if (!form.checkValidity()) {
                        form.classList.add('was-validated');
                    } else {
                        updateEducation(educationIndex);
                    }
                }, false);
            });
        }; -->