<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">Create Education Section</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Create New Education
                                    <NuxtLink :to="'/resume/education'" class="btn btn-sm btn-success float-end"><i class="bi bi-list-ol"></i>{{ ' ' }}List
                                    </NuxtLink>
                                </p>
                            </div>
                            <div class="card">
                                <div class="card-body">
                                    <form @submit.prevent="createEducation" class="form form-horizontal needs-validation"
                                        novalidate>
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="course_title">Course
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input v-model="newEducation.course_title" type="text"
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
                                                            <select v-model="newEducation.card_title"
                                                                class="form-select border-primary"
                                                                aria-label="Default select example" required>
                                                                <option disabled value="">Please Select</option>
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
                                                            <input v-model="newEducation.school_name" type="text"
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
                                                        <label class="col-md-3 label-control"
                                                            for="education_level">Education Level</label>
                                                        <div class="col-md-9">
                                                            <input v-model="newEducation.education_level" type="text"
                                                                id="education_level" class="form-control border-primary"
                                                                placeholder="Education Level" name="education_level" required>
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
                                                            <input v-model="newEducation.final_grade" type="text"
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
                                                            <input v-model="newEducation.start_date" type="date"
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
                                                            <input v-model="newEducation.end_date" type="date" id="end_date"
                                                                class="form-control border-primary" placeholder="End date"
                                                                name="end_date" required>
                                                            <span class="invalid-feedback">End date is required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                                                                
                                        <div class="row">
                                                <div class="form-actions my-2">
                                                    <NuxtLink :to="'/resume/education'" class="btn btn-sm btn-danger mx-2 float-start">
                                                <i class="bi bi-x-lg"></i>{{ ' ' }}Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-sm btn-primary mx-2 float-end">
                                                <i class="bi bi-check2-square"></i>{{ ' ' }}Save
                                            </button>
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
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
    name: 'CreateEducation',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        const axios = useNuxtApp().$axios;
        const newEducation = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });
        const router = useRouter();

        const createEducation = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/education/`,
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
            const forms = document.querySelectorAll('.needs-validation');

            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    event.preventDefault();
                    event.stopPropagation();

                    if (!form.checkValidity()) {
                        form.classList.add('was-validated');
                    } else {
                        createEducation();
                    }
                }, false);
            });
        });

        return {
            newEducation,
        };
    },
});
</script>
  
<style></style>
  