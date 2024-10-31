<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">new Certification</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Create New newCertification
                                <NuxtLink :to="'/resume/certification'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-list-ol"></i>{{ ' ' }}List
                                </NuxtLink>
                            </p>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <form @submit.prevent="createCertification"
                                    class="form form-horizontal needs-validation" novalidate>
                                    <div class="form-body">
                                        <div class="row">
                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="certified_on">Certified
                                                        On</label>
                                                    <input v-model="newCertification.certified_on" type="text"
                                                        id="certified_on" class="form-control border-primary"
                                                        placeholder="Certified On" name="certified_on" required>
                                                    <span class="invalid-feedback">Certified On is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="card_title">Card
                                                        Title</label>
                                                    <select v-model="newCertification.card_title"
                                                        class="form-select border-primary"
                                                        aria-label="Default select example" required>
                                                        <option disabled value="">Please Select</option>
                                                        <option>Certification</option>
                                                        <option>Awards</option>
                                                    </select>
                                                    <span class="invalid-feedback">Please Select Card
                                                        Title</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="school_name">School
                                                        Name</label>
                                                    <input v-model="newCertification.school_name" type="text"
                                                        id="school_name" class="form-control border-primary"
                                                        placeholder="School Name" name="school_name" required>
                                                    <span class="invalid-feedback">School Name is
                                                        required</span>
                                                </div>
                                            </div>
                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="school_type">School
                                                        Type</label>
                                                    <input v-model="newCertification.school_type" type="text"
                                                        id="school_type" class="form-control border-primary"
                                                        placeholder="School Type" name="school_type" required>
                                                    <span class="invalid-feedback">School Type is required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="start_date">Start
                                                        Date</label>
                                                    <input v-model="newCertification.start_date" type="date"
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
                                                    <input v-model="newCertification.end_date" type="date" id="end_date"
                                                        class="form-control border-primary" placeholder="End date"
                                                        name="end_date" required>
                                                    <span class="invalid-feedback">End date is required</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="row">
                                        <div class="form-actions my-2">
                                            <NuxtLink :to="'/resume/certification'"
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
    name: 'CreateCertification',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        // Set meta information
        useHead({
            title: 'Create Certification',
            meta: [
                { name: 'description', content: 'Fill in the form and submit to achieve to create new certification' },
                { property: 'og:title', content: 'Create Certification' },
                { property: 'og:description', content: 'Page to create new certification.' }
            ]
        });

        const { $axios, $showToast } = useNuxtApp();

        const newCertification = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });
        const router = useRouter();

        const createCertification = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                try {
                    await $axios.post(`/user/${user_id}/certification/`, newCertification.value);
                    $showToast("Certification created!");
                    router.push('/resume/certification');
                    console.log(response);
                } catch (error) {
                    console.log(error);
                }

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
                        createCertification();
                    }
                }, false);
            });
        });

        return {
            newCertification,
        };
    },
});
</script>

<style></style>