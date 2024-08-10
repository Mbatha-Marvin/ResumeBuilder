<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">certification Section</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Certification List
                                <NuxtLink :to="'/resume/certification/create'" class="btn btn-sm btn-success float-end">
                                    <i class="bi bi-plus-square"></i>{{ ' ' }}Create
                                </NuxtLink>
                            </p>
                        </div>
                        <div v-for="(certification, index) in certifications" :key="index" class="card mt-2">
                            <div class="card-content collapse show">
                                <div class="card-body card-dashboard">

                                    <div class="row">
                                        <p class="float-start"><strong>{{ index + 1 }}</strong></p>
                                    </div>

                                    <form @submit.prevent="submitCertificationForm(index)"
                                        class="form form-horizontal needs-validation" novalidate>
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="certified_on">Certified
                                                            On</label>
                                                        <input v-model="certification.certified_on" type="text"
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
                                                        <select v-model="certification.card_title"
                                                            class="form-select border-primary"
                                                            aria-label="Default select example" required>
                                                            <option selected :value="certification.card_title">{{
                                                                certification.card_title }}</option>
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
                                                        <input v-model="certification.school_name" type="text"
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
                                                        <input v-model="certification.school_type" type="text"
                                                            id="school_type" class="form-control border-primary"
                                                            placeholder="School Type" name="school_type" required>
                                                        <span class="invalid-feedback">School Type is required</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="start_date">Start
                                                            Date</label>
                                                        <input v-model="certification.start_date" type="date"
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
                                                        <input v-model="certification.end_date" type="date"
                                                            id="end_date" class="form-control border-primary"
                                                            placeholder="End date" name="end_date" required>
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

                                                <button @click="deleteCertification(certification.certification_id)"
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
    name: 'certificationList',
    setup() {


        definePageMeta({
            layout: "sidestar",
        });

        // Set meta information
        useHead({
            title: 'Certification List',
            meta: [
                { name: 'description', content: 'View Certification List' },
                { property: 'og:title', content: 'Certification List' },
                { property: 'og:description', content: 'View Certification List.' }
            ]
        });

        const certifications = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;
        const router = useRouter();

        const getertification = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/certification/`);
                certifications.value = response.data;
            } catch (error) {
                console.error('Error fetching certifications:', error);
            }
        };

        const updateCertification = async (certificationIndex) => {
            try {
                await axios.patch(
                    `/user/${certificationIndex.user_id}/certification/${certificationIndex.certification_id}`,
                    certificationIndex
                ).then(function (response) {
                    console.log(response);
                    router.push('/resume/certification');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteCertification = async (certification_id) => {
            try {
                await axios.delete(`/user/${user_id}/certification/${certification_id}`);
                getertification();
            } catch (error) {
                console.error('Error deleting certification:', error);
            }
        };

        const submitCertificationForm = async (certificationIndex) => {
            const certificationToUpdate = certifications.value[certificationIndex];
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            updateCertification(certificationToUpdate);
        };

        onMounted(() => {
            getertification();
        });

        return {
            certifications,
            deleteCertification,
            submitCertificationForm
        };
    },
});
</script>

<style></style>