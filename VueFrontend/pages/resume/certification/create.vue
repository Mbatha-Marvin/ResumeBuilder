<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">newCertification</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Create New newCertification
                                    <NuxtLink :to="'/resume/certification'" class="btn btn-sm btn-success float-end"><i class="bi bi-list-ol"></i>{{ ' ' }}List
                                    </NuxtLink>
                                </p>
                            </div>
                            <div class="card">
                                <div class="card-body">
                                    <form @submit.prevent="createCertification"
                                            class="form form-horizontal needs-validation" novalidate>
                                            <div class="form-body">
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="certified_on">Certified On</label>
                                                            <div class="col-md-9">
                                                                <input v-model="newCertification.certified_on" type="text"
                                                                    id="certified_on" class="form-control border-primary"
                                                                    placeholder="Certified On" name="certified_on" required>
                                                                <span class="invalid-feedback">Certified On is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="card_title">Card
                                                                Title</label>
                                                            <div class="col-md-9">
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
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="school_name">School
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="newCertification.school_name" type="text"
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
                                                                for="school_type">School Type</label>
                                                            <div class="col-md-9">
                                                                <input v-model="newCertification.school_type" type="text"
                                                                    id="school_type" class="form-control border-primary"
                                                                    placeholder="School Type" name="school_type" required>
                                                                <span class="invalid-feedback">School Type is required</span>
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
                                                                <input v-model="newCertification.start_date" type="date"
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
                                                                <input v-model="newCertification.end_date" type="date"
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
                                                    <NuxtLink :to="'/resume/certification'" class="btn btn-sm btn-danger mx-2 float-start">
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
    name: 'CreateCertification',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        const axios = useNuxtApp().$axios;
        const newCertification = ref({ card_title: '', school_name: '', education_level: '', course_title: '', location: '', final_grade: '', start_date: '', end_date: '' });
        const router = useRouter();

        const createCertification = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/certification/`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newCertification.value),
                })
                    .then(function (response) {
                        router.push('/resume/certification');
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
  