<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Experience Section</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Create New Experience
                                <NuxtLink :to="'/resume/experience'" class="btn btn-sm btn-success float-end"><i
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
                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="job_title">Job
                                                        Title</label>
                                                    <input v-model="newExperience.job_title" type="text" id="job_title"
                                                        class="form-control border-primary" placeholder="Job title"
                                                        name="job_title" required>
                                                    <span class="invalid-feedback">Job title is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="card_title">Card
                                                        Title</label>
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

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="company_name">Company
                                                        Name</label>
                                                    <input v-model="newExperience.company_name" type="text"
                                                        id="company_name" class="form-control border-primary"
                                                        placeholder="Company Name" name="company_name" required>
                                                    <span class="invalid-feedback">Company Name is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="company_url">Company
                                                        Url</label>
                                                    <input v-model="newExperience.company_url" type="text"
                                                        id="company_url" class="form-control border-primary"
                                                        placeholder="Company Url" name="company_url" required>
                                                    <span class="invalid-feedback">Company Url is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="location">Location</label>
                                                    <input v-model="newExperience.location" type="text" id="location"
                                                        class="form-control border-primary" placeholder="Location"
                                                        name="location" required>
                                                    <span class="invalid-feedback">Location is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="start_date">Start
                                                        Date</label>
                                                    <input v-model="newExperience.start_date" type="date"
                                                        id="start_date" class="form-control border-primary" placeholder="Start
                                                            Date" name="start_date" required>
                                                    <span class="invalid-feedback">Start
                                                        Date is required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="end_date">End
                                                        date</label>
                                                    <input v-model="newExperience.end_date" type="date" id="end_date"
                                                        class="form-control border-primary" placeholder="End date"
                                                        name="end_date" required>
                                                    <span class="invalid-feedback">End date is required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="location">Description:</label>
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

                                                <div v-if="newExperience.job_descriptions.length > 0" class="card mb-2">
                                                    <div class="card-content collapse show">
                                                        <div class="card-body card-dashboard">
                                                            <div class="row">
                                                                <p>job descriptions here</p>
                                                                <hr class="border border-primary border-1 opacity-50">
                                                            </div>

                                                            <ol type="1">
                                                                <li v-for="(description, descriptionIndex) in newExperience.job_descriptions"
                                                                    :key="descriptionIndex" class="my-1">{{
                                                                        description
                                                                    }} <i
                                                                        @click="removeDescription(index, descriptionIndex)"
                                                                        class="bi bi-x bg-danger text-white"></i></li>
                                                            </ol>
                                                        </div>
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
                                            <button type="submit" class="btn btn-sm btn-success mx-2 float-end">
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

        // Set meta information
        useHead({
            title: 'Create Experience',
            meta: [
                { name: 'description', content: 'Form to Create Experience' },
                { property: 'og:title', content: 'Create Experience' },
                { property: 'og:description', content: 'Form to Create Experience.' }
            ]
        });

        const axios = useNuxtApp().$axios;
        const newExperience = ref({ card_title: '', job_title: '', company_name: '', company_url: '', location: '', job_description_title: '', job_descriptions: [], start_date: '', end_date: '' });
        const newDescription = ref('');
        const router = useRouter();

        const addDescription = () => {

            if (newDescription.value.trim() !== '') {
                const experienceDescriptionToAdd = newExperience.value.job_descriptions;
                if (experienceDescriptionToAdd.length < 5) {
                    experienceDescriptionToAdd.push(newDescription.value);
                } else {
                    console.log('Errow while adding, exceeded 5');
                }

                newDescription.value = '';
            }
        };

        const removeDescription = (descriptionIndex) => {
            const experienceDescriptionToremove = newExperience.value.job_descriptions;
            experienceDescriptionToremove.splice(descriptionIndex, 1)
        };

        const createExperience = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/experience/`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newExperience.value),
                })
                    .then(function (response) {
                        router.push('/resume/experience');
                        // console.log(response);
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
            newDescription,
            removeDescription
        };
    },
});
</script>

<style></style>