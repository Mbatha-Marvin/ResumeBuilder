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
                                <p class="d-inline">Update Education Details
                                    <NuxtLink :to="'/resume/education'" class="btn btn-sm btn-danger float-end"><i
                                            class="bi bi-arrow-left-circle"></i>Back
                                    </NuxtLink>
                                </p>
                            </div>
                            <div class="card">
                                <div class="card-body">
                                    <!-- <form class="form form-horizontal">
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="course_title">Course
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="course_title"
                                                                class="form-control border-primary" placeholder="Course Title" name="course_title">
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="col-md-6 invisible">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="card_title">Card
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="card_title"
                                                                class="form-control border-primary" value="Education" placeholder="Card Title"
                                                                name="card_title">
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
                                                            <input type="text" id="school_name"
                                                                class="form-control border-primary" placeholder="School Name" name="school_name">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="location">Location</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="location"
                                                                class="form-control border-primary" placeholder="Location"
                                                                name="location">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="education_level">Education Level</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="education_level"
                                                                class="form-control border-primary" placeholder="Education Level" name="education_level">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="final_grade">Final
                                                            Grade</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="final_grade"
                                                                class="form-control border-primary" placeholder="Final Grade" name="final_grade">
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
                                                            <input type="date" id="start_date"
                                                                class="form-control border-primary" placeholder="Start
                                                            Date" name="start_date">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="end_date">End
                                                            date</label>
                                                        <div class="col-md-9">
                                                            <input type="date" id="end_date"
                                                                class="form-control border-primary" placeholder="End date"
                                                                name="end_date">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="form-actions float-end mt-2">
                                            <NuxtLink :to="'/resume/education/create'" class="btn btn-danger mx-2">
                                                <i class="bi bi-x-lg"></i> Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-primary mx-2">
                                                <i class="bi bi-check2-square"></i> Update
                                            </button>
                                        </div>
                                    </form> -->

                                    <form @submit.prevent="updateEducation" class="form form-horizontal needs-validation"
                                        novalidate>
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="course_title">Course
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input v-model="editEducation.course_title" type="text"
                                                                id="course_title" class="form-control border-primary"
                                                                placeholder="Course Title" name="course_title" required>
                                                            <span class="invalid-feedback">Course Title is required</span>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="card_title">Card
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <select v-model="editEducation.card_title"
                                                                class="form-select border-primary"
                                                                aria-label="Default select example" required>
                                                                <option selected :value="editEducation.card_title">{{
                                                                    editEducation.card_title }}</option>
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
                                                            <input v-model="editEducation.school_name" type="text"
                                                                id="school_name" class="form-control border-primary"
                                                                placeholder="School Name" name="school_name" required>
                                                            <span class="invalid-feedback">School Name is required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="location">Location</label>
                                                        <div class="col-md-9">
                                                            <input v-model="editEducation.location" type="text"
                                                                id="location" class="form-control border-primary"
                                                                placeholder="Location" name="location" required>
                                                            <span class="invalid-feedback">Location is required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="education_level">Education Level</label>
                                                        <div class="col-md-9">
                                                            <input v-model="editEducation.education_level" type="text"
                                                                id="education_level" class="form-control border-primary"
                                                                placeholder="Education Level" name="education_level"
                                                                required>
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
                                                            <input v-model="editEducation.final_grade" type="text"
                                                                id="final_grade" class="form-control border-primary"
                                                                placeholder="Final Grade" name="final_grade" required>
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
                                                            <input v-model="editEducation.start_date" type="date"
                                                                id="start_date" class="form-control border-primary"
                                                                placeholder="Start
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
                                                            <input v-model="editEducation.end_date" type="date"
                                                                id="end_date" class="form-control border-primary"
                                                                placeholder="End date" name="end_date" required>
                                                            <span class="invalid-feedback">End date is required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="form-actions float-end mt-2">
                                            <NuxtLink :to="'/resume/education'" class="btn btn-danger mx-2">
                                                <i class="bi bi-x-lg"></i> Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-primary mx-2">
                                                <i class="bi bi-check2-square"></i> Save
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
</template>
  
<script>
import { defineComponent, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default defineComponent({
    name: 'editEducation',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        const axios = useNuxtApp().$axios;
        const editEducation = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });

        const route = useRoute();
        const router = useRouter();
        const user_id = 1;

        console.log(route.params.education_id);

        const getEducation = async () => {
            await axios({
                method: 'get',
                url: `/user/${user_id}/education/${route.params.education_id}`,
                headers: { 'Content-Type': 'application/json' },
            })
                .then(function (response) {
                    editEducation.value = response.data;
                    console.log(response);
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
                    url: `/user/${user_id}/education/${route.params.education_id}`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newEducation.value),
                })
                    .then(function (response) {
                        router.push('/resume/education');
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            } else {
                form.classList.add('was-validated');
            };
        };

        onMounted(() => {

            if (getEducation()) {
                getEducation();
            } else {
                const forms = document.querySelectorAll('.needs-validation');
                Array.from(forms).forEach(form => {
                    form.addEventListener('submit', event => {
                        event.preventDefault();
                        event.stopPropagation();

                        if (!form.checkValidity()) {
                            form.classList.add('was-validated');
                        } else {
                            updateEducation();
                        }
                    }, false);
                });
            }
        });

        return {
            editEducation,
            updateEducation,
        };
    },
});
</script>
  
<style></style>
  


















<!-- 


<script>
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
    name: 'EducationList',
    setup() {
        const educations = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;

        const getEducation = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/education/`);
                educations.value = response.data;
            } catch (error) {
                console.error('Error fetching educations:', error);
            }
        };

        const updateEducation = async (education) => {
            try {
                await axios.patch(`/user/${user_id}/education/${education.education_id}`, education);
            } catch (error) {
                console.error('Error updating education:', error);
            }
        };

        const deleteEducation = async (education_id) => {
            try {
                await axios.delete(`/user/${user_id}/education/${education_id}`);
                getEducation();
            } catch (error) {
                console.error('Error deleting education:', error);
            }
        };

        const submitEducationForm = async (educationIndex) => {
            const educationToUpdate = educations.value[educationIndex];
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            updateEducation(educationToUpdate);
        };

        onMounted(() => {
            getEducation();
        });

        return {
            educations,
            deleteEducation,
            submitEducationForm
        };
    },
});
</script>

<style></style> -->
