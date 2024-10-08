<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">

            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Referee Section</h4>
                </div>
            </div>

            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Referee List
                                <NuxtLink :to="'/resume/referee/create'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-plus-square"></i>{{ ' ' }}Create
                                </NuxtLink>
                            </p>
                        </div>
                        <div v-for="(referee, index) in referees" :key="index" class="card mt-2">
                            <div class="card-content collapse show">
                                <div class="card-body card-dashboard">

                                    <div class="row">
                                        <p class="float-start"><strong>{{ index + 1 }}</strong></p>
                                    </div>

                                    <form @submit.prevent="submitRefereeForm(index)"
                                        class="form form-horizontal needs-validation" novalidate>
                                        <div class="form-body">
                                            <div class="row">

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="card_title">Card
                                                            Title</label>
                                                        <select v-model="referee.card_title"
                                                            class="form-select border-primary"
                                                            aria-label="Default select example" required>
                                                            <option selected :value="referee.card_title">{{
                                                                referee.card_title }}</option>
                                                            <option>Referee</option>
                                                            <option>Reference</option>
                                                        </select>
                                                        <span class="invalid-feedback">Please Select Card
                                                            Title</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="full_name">Referee
                                                            Name</label>
                                                        <input v-model="referee.full_name" type="text" id="full_name"
                                                            class="form-control border-primary"
                                                            placeholder="Referee Name" name="full_name" required>
                                                        <span class="invalid-feedback">Referee Name is
                                                            required</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="phone_number">Phone
                                                            Number</label>
                                                        <input v-model="referee.phone_number" type="text"
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
                                                        <input v-model="referee.company_name" type="text"
                                                            id="company_name" class="form-control border-primary"
                                                            placeholder="Company Name" name="company_name" required>
                                                        <span class="invalid-feedback">Company Name is
                                                            required</span>
                                                    </div>
                                                </div>

                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="occupation">Occupation</label>
                                                        <input v-model="referee.occupation" type="text" id="occupation"
                                                            class="form-control border-primary" placeholder="Occupation"
                                                            name="occupation" required>
                                                        <span class="invalid-feedback">Occupation is
                                                            required</span>
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <div class="form-group mb-2">
                                                        <label class="label-control" for="address">Address</label>
                                                        <input v-model="referee.address" type="text" id="address"
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
                                                <button type="submit" class="btn btn-sm btn-warning mx-2 float-start">
                                                    <i class="bi bi-pencil-square"></i>{{ ' ' }}Update
                                                </button>

                                                <button @click="deleteReferee(referee.referee_id)"
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
    name: 'refereeList',

    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        // Set meta information
        useHead({
            title: 'Referees',
            meta: [
                { name: 'description', content: 'View Referees' },
                { property: 'og:title', content: 'Referees' },
                { property: 'og:description', content: 'View Referees.' }
            ]
        });

        const referees = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;
        const router = useRouter();

        const getReferee = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/referee/`);
                referees.value = response.data;
            } catch (error) {
                console.error('Error fetching referees:', error);
            }
        };

        const updateReferee = async (refereeIndex) => {
            try {
                await axios.patch(
                    `/user/${refereeIndex.user_id}/referee/${refereeIndex.referee_id}`,
                    refereeIndex
                ).then(function (response) {
                    console.log(response);
                    router.push('/resume/referee');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteReferee = async (referee_id) => {
            try {
                await axios.delete(`/user/${user_id}/referee/${referee_id}`);
                getReferee();
            } catch (error) {
                console.error('Error deleting referee:', error);
            }
        };

        const submitRefereeForm = async (refereeIndex) => {
            const refereeToUpdate = referees.value[refereeIndex];
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            updateReferee(refereeToUpdate);
        };

        onMounted(() => {
            getReferee();
        });

        return {
            referees,
            deleteReferee,
            submitRefereeForm
        };
    },
});
</script>

<style></style>