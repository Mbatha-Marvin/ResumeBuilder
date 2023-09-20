<template>
    <div class="container py-5">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">Experience Section</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Experience List
                                    <NuxtLink :to="'/resume/experience/create'" class="btn btn-sm btn-success float-end"><i
                                            class="bi bi-plus-square"></i>{{ ' ' }}Create
                                    </NuxtLink>
                                </p>
                            </div>
                            <div v-for="(experience, index) in experiences" :key="index" class="card mt-2">
                                <div class="card-content collapse show">
                                    <div class="card-body card-dashboard">

                                        <div class="row">
                                            <p class="float-start"><strong>{{ index + 1 }}</strong></p>
                                        </div>

                                        <form @submit.prevent="submitExperienceForm(index)"
                                            class="form form-horizontal needs-validation" novalidate>
                                            <div class="form-body">
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="job_title">Job
                                                                Title</label>
                                                            <div class="col-md-9">
                                                                <input v-model="experience.job_title" type="text"
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
                                                                <select v-model="experience.card_title"
                                                                    class="form-select border-primary"
                                                                    aria-label="Default select example" required>
                                                                    <option selected :value="experience.card_title">{{
                                                                        experience.card_title }}</option>
                                                                    <option>Experience</option>
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
                                                                <input v-model="experience.company_name" type="text"
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
                                                                <input v-model="experience.company_url" type="text"
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
                                                                <input v-model="experience.location" type="text"
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
                                                                            @click="addDescription(index)"><i
                                                                                class="bi bi-plus"></i></button></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="card mb-2">
                                                            <div class="card-content collapse show">
                                                                <div class="card-body card-dashboard">
                                                                    <div class="row">
                                                                        <p>job descriptions here</p>
                                                                        <Bold_hr />
                                                                    </div>

                                                                    <ol type="1">
                                                                        <li v-for="(description, descriptionIndex) in experience.job_descriptions"
                                                                            :key="descriptionIndex" class="my-2 mx-2">{{
                                                                                description }} <button type="button"
                                                                                class="btn btn-sm btn-danger"
                                                                                @click="removeDescription(index, descriptionIndex)"><i
                                                                                    class="bi bi-x"></i></button></li>
                                                                    </ol>

                                                                </div>
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
                                                                <input v-model="experience.start_date" type="date"
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
                                                                <input v-model="experience.end_date" type="date"
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
                                                    <button type="submit" class="btn btn-sm btn-primary mx-2 float-start">
                                                        <i class="bi bi-pencil-square"></i>{{ ' ' }}Update
                                                    </button>

                                                    <button @click="deleteExperience(experience.experience_id)"
                                                        class="btn btn-sm btn-danger float-end mx-2"><i
                                                            class="bi bi-trash3"></i>
                                                        {{ ' ' }}Delete
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
    </div>
</template>
  
<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Bold_hr from '../../../components/Helpers/Bold_hr.vue';

definePageMeta({
    layout: "sidestar",
});

export default defineComponent({
    name: 'experienceList',
    setup() {
        const experiences = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;
        const router = useRouter();
        const newDescription = ref('');

        const getExperience = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/experience/`);
                experiences.value = response.data;
            }
            catch (error) {
                console.error('Error fetching experiences:', error);
            }
        };
        const updateExperience = async (experienceIndex) => {
            try {
                await axios.patch(`/user/${experienceIndex.user_id}/experience/${experienceIndex.experience_id}`, experienceIndex).then(function (response) {
                    console.log(response);
                    router.push('/resume/experience');
                });
            }
            catch (error) {
                console.error('Error updating:', error);
            }
        };
        const deleteExperience = async (experience_id) => {
            try {
                await axios.delete(`/user/${user_id}/experience/${experience_id}`);
                getExperience();
            }
            catch (error) {
                console.error('Error deleting experience:', error);
            }
        };
        const addDescription = (experienceIndex) => {
            if (newDescription.value.trim() !== '') {
                const experienceDescriptionToAdd = experiences.value[experienceIndex];
                if (experienceDescriptionToAdd.job_descriptions.length < 5) {
                    experienceDescriptionToAdd.job_descriptions.push(newDescription.value);
                }
                else {
                    console.log('Errow while adding, exceeded 5');
                }
                newDescription.value = '';
            }
        };
        const removeDescription = (experienceIndex, descriptionIndex) => {
            const experienceDescriptionToremove = experiences.value[experienceIndex];
            experienceDescriptionToremove.job_descriptions.splice(descriptionIndex, 1);
        };
        const submitExperienceForm = async (experienceIndex) => {
            const experienceToUpdate = experiences.value[experienceIndex];
            const form = document.querySelector('.needs-validation');
            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }
            updateExperience(experienceToUpdate);
        };
        onMounted(() => {
            getExperience();
        });
        return {
            experiences,
            deleteExperience,
            submitExperienceForm,
            addDescription,
            newDescription,
            removeDescription,
        };
    },
    components: { Bold_hr }
});
</script>
  
<style></style>
  