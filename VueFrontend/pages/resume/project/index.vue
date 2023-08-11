<template>
    <div class="container">
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
                                <h4 class="d-inline">Experience List
                                    <NuxtLink :to="'/resume/experience/create'" class="btn btn-sm btn-success float-end"><i
                                            class="bi bi-plus-square"></i>{{ ' ' }}Create
                                    </NuxtLink>
                                </h4>
                            </div>
                            <div v-for="(experience, index) in experiences" :key="index" class="card mt-2">
                                <div class="card-content collapse show">
                                    <div class="card-body card-dashboard">

                                        <div class="row">
                                            <p class="float-start"><strong>{{ index }}</strong></p>
                                        </div>

                                        <form @submit.prevent="submitExperienceForm(index)"
                                            class="form form-horizontal needs-validation" novalidate>
                                            <div class="form-body">
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="course_title">Course
                                                                Title</label>
                                                            <div class="col-md-9">
                                                                <input v-model="experience.course_title" type="text"
                                                                    id="course_title" class="form-control border-primary"
                                                                    placeholder="Course Title" name="course_title" required>
                                                                <span class="invalid-feedback">Course Title is
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
                                                                    <option>experience</option>
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
                                                            <label class="col-md-3 label-control" for="school_name">School
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="experience.school_name" type="text"
                                                                    id="school_name" class="form-control border-primary"
                                                                    placeholder="School Name" name="school_name" required>
                                                                <span class="invalid-feedback">School Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="location">Location</label>
                                                            <div class="col-md-9">
                                                                <input v-model="experience.location" type="text"
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
                                                                for="experience_level">experience
                                                                Level</label>
                                                            <div class="col-md-9">
                                                                <input v-model="experience.experience_level" type="text"
                                                                    id="experience_level"
                                                                    class="form-control border-primary"
                                                                    placeholder="experience Level" name="experience_level"
                                                                    required>
                                                                <span class="invalid-feedback">experience Level is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="final_grade">Final
                                                                Grade</label>
                                                            <div class="col-md-9">
                                                                <input v-model="experience.final_grade" type="text"
                                                                    id="final_grade" class="form-control border-primary"
                                                                    placeholder="Final Grade" name="final_grade" required>
                                                                <span class="invalid-feedback">Final Grade is
                                                                    required</span>
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

        const getExperience = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/experience/`);
                experiences.value = response.data;
            } catch (error) {
                console.error('Error fetching experiences:', error);
            }
        };

        const updateExperience = async (experienceIndex) => {
            try {
                await axios.patch(
                    `/user/${experienceIndex.user_id}/experience/${experienceIndex.experience_id}`,
                    experienceIndex
                ).then(function (response) {
                    console.log(response);
                    router.push('/resume/experience');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteExperience = async (experience_id) => {
            try {
                await axios.delete(`/user/${user_id}/experience/${experience_id}`);
                getExperience();
            } catch (error) {
                console.error('Error deleting experience:', error);
            }
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
            submitExperienceForm
        };
    },
});
</script>
  
<style></style>
  