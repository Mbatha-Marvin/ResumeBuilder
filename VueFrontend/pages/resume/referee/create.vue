<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Referee</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Create New Referee
                                <NuxtLink :to="'/resume/referee'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-list-ol"></i>{{ ' ' }}List
                                </NuxtLink>
                            </p>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <form @submit.prevent="createnewReferee" class="form form-horizontal needs-validation"
                                    novalidate>
                                    <div class="form-body">
                                        <div class="row">

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="card_title">Card
                                                        Title</label>
                                                    <select v-model="newReferee.card_title"
                                                        class="form-select border-primary"
                                                        aria-label="Default select example" required>
                                                        <option disabled value="">Please Select</option>
                                                        <option>Referee</option>
                                                        <option>Reference</option>
                                                    </select>
                                                    <span class="invalid-feedback">Please Select Card
                                                        Title</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="full_name">Full
                                                        Name</label>
                                                    <input v-model="newReferee.full_name" type="text" id="full_name"
                                                        class="form-control border-primary" placeholder="Full Name"
                                                        name="full_name" required>
                                                    <span class="invalid-feedback">Full Name is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="phone_number">Phone
                                                        Number</label>
                                                    <input v-model="newReferee.phone_number" type="text"
                                                        id="phone_number" class="form-control border-primary"
                                                        placeholder="Phone Number" name="phone_number" required>
                                                    <span class="invalid-feedback">Phone Number is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="company_name">Company
                                                        Name</label>
                                                    <input v-model="newReferee.company_name" type="text"
                                                        id="company_name" class="form-control border-primary"
                                                        placeholder="Company Name" name="company_name" required>
                                                    <span class="invalid-feedback">Company Name is required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="occupation">Occupation</label>
                                                    <input v-model="newReferee.occupation" type="text" id="occupation"
                                                        class="form-control border-primary" placeholder="Occupation"
                                                        name="occupation" required>
                                                    <span class="invalid-feedback">Occupation is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="address">Address</label>
                                                    <input v-model="newReferee.address" type="text" id="address"
                                                        class="form-control border-primary" placeholder="Address"
                                                        name="address" required>
                                                    <span class="invalid-feedback">Address is
                                                        required</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="row">
                                        <div class="form-actions my-2">
                                            <NuxtLink :to="'/resume/referee'"
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
    name: 'CreateReferee',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        // Set meta information
        useHead({
            title: 'Create Referee',
            meta: [
                { name: 'description', content: 'Form to Create Referee' },
                { property: 'og:title', content: 'Create Referee' },
                { property: 'og:description', content: 'Form to Create Referee.' }
            ]
        });
        const axios = useNuxtApp().$axios;
        const newReferee = ref({});
        const router = useRouter();

        const createnewReferee = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            form.addEventListener('submit', event => {
                event.preventDefault();
                event.stopPropagation();

                if (!form.checkValidity()) {
                    form.classList.add('was-validated');
                } else {
                    axios({
                        method: 'post',
                        url: `/user/${user_id}/referee/`,
                        headers: { 'Content-Type': 'application/json' },
                        data: JSON.stringify(newReferee.value),
                    })
                        .then(function (response) {
                            router.push('/resume/referee');
                            console.log(response);
                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                }
            }, false);
        };

        onMounted(() => {
            createnewReferee();
        });

        return {
            newReferee,
        };
    },
});
</script>

<style></style>