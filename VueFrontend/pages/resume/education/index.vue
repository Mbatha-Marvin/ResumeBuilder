<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Education List Section</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Education List
                                <NuxtLink :to="'/resume/education/create'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-plus-square"></i>{{ ' ' }}Create
                                </NuxtLink>
                            </p>
                        </div>
                        <div v-for="(education, index) in educations" :key="index" class="card mt-2">
                            <div class="card-content collapse show">
                                <div class="card-body card-dashboard">

                                    <div class="row">
                                        <p class="float-start"><strong>{{ index + 1 }}</strong></p>
                                    </div>

                                    <form @submit.prevent="submitEducationForm(index)"
                                        class="form form-horizontal needs-validation" novalidate>
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="course_title">Course
                                                            Title</label>
                                                        <input v-model="education.course_title" type="text"
                                                            id="course_title" class="form-control border-primary"
                                                            placeholder="Course Title" name="course_title" required>
                                                        <span class="invalid-feedback">Course Title is
                                                            required</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="card_title">Card
                                                            Title</label>
                                                        <select v-model="education.card_title"
                                                            class="form-select border-primary"
                                                            aria-label="Default select example" required>
                                                            <option selected :value="education.card_title">{{
                                                                education.card_title }}</option>
                                                            <option>Education</option>
                                                            <option>Academics</option>
                                                        </select>
                                                        <span class="invalid-feedback">Please Select Card
                                                            Title</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="school_name">School
                                                            Name</label>
                                                        <input v-model="education.school_name" type="text"
                                                            id="school_name" class="form-control border-primary"
                                                            placeholder="School Name" name="school_name" required>
                                                        <span class="invalid-feedback">School Name is
                                                            required</span>
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="location">Location</label>
                                                        <input v-model="education.location" type="text" id="location"
                                                            class="form-control border-primary" placeholder="Location"
                                                            name="location" required>
                                                        <span class="invalid-feedback">Location is required</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="education_level">Education
                                                            Level</label>
                                                        <input v-model="education.education_level" type="text"
                                                            id="education_level" class="form-control border-primary"
                                                            placeholder="Education Level" name="education_level"
                                                            required>
                                                        <span class="invalid-feedback">Education Level is
                                                            required</span>
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="final_grade">Final
                                                            Grade</label>
                                                        <input v-model="education.final_grade" type="text"
                                                            id="final_grade" class="form-control border-primary"
                                                            placeholder="Final Grade" name="final_grade" required>
                                                        <span class="invalid-feedback">Final Grade is
                                                            required</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="start_date">Start
                                                            Date</label>
                                                        <input v-model="education.start_date" type="date"
                                                            id="start_date" class="form-control border-primary"
                                                            placeholder="Start
                                                            Date" name="start_date" required>
                                                        <span class="invalid-feedback">Start
                                                            Date is required</span>
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="end_date">End
                                                            date</label>
                                                        <input v-model="education.end_date" type="date" id="end_date"
                                                            class="form-control border-primary" placeholder="End date"
                                                            name="end_date" required>
                                                        <span class="invalid-feedback">End date is required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="form-actions my-2">
                                                <button type="submit" class="btn btn-sm btn-warning mx-2 float-start">
                                                    <i class="bi bi-pencil-square"></i>{{ ' ' }}Update
                                                </button>

                                                <button @click="deleteEducation(education.education_id)"
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
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';


export default defineComponent({
    name: 'EducationList',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        // Set meta information
        useHead({
            title: 'Education',
            meta: [
                { name: 'description', content: 'View Education List' },
                { property: 'og:title', content: 'Education List' },
                { property: 'og:description', content: 'View Education List.' }
            ]
        });

        const educations = ref([]);
        const { $axios, $showToast } = useNuxtApp();
        const user_id = 1;
        const router = useRouter();

        const getEducation = async () => {
            try {
                const response = await $axios.get(`/user/${user_id}/education/`);
                educations.value = response.data;
            } catch (error) {
                console.error('Error fetching educations:', error);
            }
        };

        const updateEducation = async (educationIndex) => {
            try {
                await $axios.patch(
                    `/user/${educationIndex.user_id}/education/${educationIndex.education_id}`,
                    educationIndex
                ).then(function (response) {
                    console.log(response);
                    $showToast("Education updated!");
                    router.push('/resume/education');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteEducation = async (education_id) => {
            try {
                await $axios.delete(`/user/${user_id}/education/${education_id}`);
                $showToast("Education deleted!");
                getEducation();
            } catch (error) {
                console.error('Error deleting education:', error);
            }
        };

        const submitEducationForm = async (educationIndex) => {
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            const educationToUpdate = educations.value[educationIndex];

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

<style></style>