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
                                <p class="d-inline">Create New Education
                                    <NuxtLink :to="'/resume/education'" class="btn btn-sm btn-success float-end"><i
                                            class="bi bi-list-ol"></i>{{ ' ' }}List
                                    </NuxtLink>
                                </p>
                            </div>
                            <div class="card">
                                <div class="card-body">
                                    <form @submit.prevent="submitnewExperienceForm"
                                        class="form form-horizontal needs-validation" novalidate>
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="job_title">Job
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input v-model="newExperience.job_title" type="text"
                                                                id="job_title" class="form-control border-primary"
                                                                placeholder="Job title" name="job_title" required>
                                                            <span class="invalid-feedback">Job title is
                                                                required</span>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="card_title">Card
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <select v-model="newExperience.card_title"
                                                                class="form-select border-primary"
                                                                aria-label="Default select example" required>
                                                                <option disabled value="">Please Select</option>
                                                                <option>Education</option>
                                                                <option>Academics</option>
                                                            </select>
                                                            <span class="invalid-feedback">Please Select Card
                                                                Title</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="company_name">Company
                                                            Name</label>
                                                        <div class="col-md-9">
                                                            <input v-model="newExperience.company_name" type="text"
                                                                id="company_name" class="form-control border-primary"
                                                                placeholder="Company Name" name="company_name" required>
                                                            <span class="invalid-feedback">Company Name is
                                                                required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="company_url">Company
                                                            Url</label>
                                                        <div class="col-md-9">
                                                            <input v-model="newExperience.company_url" type="text"
                                                                id="company_url" class="form-control border-primary"
                                                                placeholder="Company Url" name="company_url" required>
                                                            <span class="invalid-feedback">Company Url is
                                                                required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="location">Location</label>
                                                        <div class="col-md-9">
                                                            <input v-model="newExperience.location" type="text"
                                                                id="location" class="form-control border-primary"
                                                                placeholder="Location" name="location" required>
                                                            <span class="invalid-feedback">Location is
                                                                required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="location">Description:</label>
                                                        <div class="col-md-9">
                                                            <div class="input-group">
                                                                <input v-model="newDescription" type="text"
                                                                    class="form-control border-primary"
                                                                    placeholder="Type and click (+) to add to list" />
                                                                <span class="input-group-text"><button
                                                                        class="btn btn-sm btn-success" type="button"
                                                                        @click="addDescription"><i
                                                                            class="bi bi-plus"></i></button></span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="col-md-6">
                                                    <div class="card mb-2">
                                                        <div v-for="(description, descriptionIndex) in newExperience.job_descriptions"
                                                            :key="descriptionIndex" class="description-entry my-2 mx-2">
                                                            {{ description }}
                                                            <button type="button" class="btn btn-sm btn-danger"
                                                                @click="removeDescription(index, descriptionIndex)"><i
                                                                    class="bi bi-x"></i></button>
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
                                                            <input v-model="newExperience.start_date" type="date"
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
                                                            <input v-model="newExperience.end_date" type="date"
                                                                id="end_date" class="form-control border-primary"
                                                                placeholder="End date" name="end_date" required>
                                                            <span class="invalid-feedback">End date is required</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="form-actions my-2">
                                                <NuxtLink :to="'/resume/experience'"
                                                    class="btn btn-sm btn-danger mx-2 float-start">
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
    name: 'createExperience',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        const axios = useNuxtApp().$axios;
        const newExperience = ref({});
        const router = useRouter();

        const addDescription = (experienceIndex) => {
            if (newDescription.value.trim() !== '') {
                const experienceDescriptionToAdd = experiences.value[experienceIndex];
                if (experienceDescriptionToAdd.job_descriptions.length < 5) {
                    experienceDescriptionToAdd.job_descriptions.push(newDescription.value);
                } else {
                    console.log('Errow while adding, exceeded 5');
                }

                newDescription.value = '';
            }
        };

        const removeDescription = (experienceIndex, descriptionIndex) => {
            const experienceDescriptionToremove = experiences.value[experienceIndex];
            experienceDescriptionToremove.job_descriptions.splice(descriptionIndex, 1)
        };

        const createExperience = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/education/`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newExperience.value),
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
                        createExperience();
                    }
                }, false);
            });
        });

        return {
            newExperience,
            addDescription,
            removeDescription
        };
    },
});
</script>
  
<style></style>
  