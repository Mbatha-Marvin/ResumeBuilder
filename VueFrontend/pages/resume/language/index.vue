<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">language Section</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <h4 class="d-inline">language List
                                    <NuxtLink :to="'/resume/language/create'" class="btn btn-sm btn-success float-end"><i
                                            class="bi bi-plus-square"></i>{{ ' ' }}Create
                                    </NuxtLink>
                                </h4>
                            </div>
                            <div v-for="(language, index) in languages" :key="index" class="card mt-2">
                                <div class="card-content collapse show">
                                    <div class="card-body card-dashboard">

                                        <div class="row">
                                            <p class="float-start"><strong>{{ index }}</strong></p>
                                        </div>

                                        <form @submit.prevent="submitLanguageForm(index)"
                                            class="form form-horizontal needs-validation" novalidate>
                                            <div class="form-body">
                                                <div class="row">
                                                    
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="card_title">Card
                                                                Title</label>
                                                            <div class="col-md-9">
                                                                <select v-model="language.card_title"
                                                                    class="form-select border-primary"
                                                                    aria-label="Default select example" required>
                                                                    <option selected :value="language.card_title">{{
                                                                        language.card_title }}</option>
                                                                    <option>Language</option>
                                                                    <option>Spoken Language</option>
                                                                </select>
                                                                <span class="invalid-feedback">Please Select Card
                                                                    Title</span>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="language_name">language Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="language.language_name" type="text"
                                                                    id="language_name" class="form-control border-primary"
                                                                    placeholder="language Name" name="language_name" required>
                                                                <span class="invalid-feedback">language Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>

                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="profeciency_level">Proficiency Level</label>
                                                            <div class="col-md-9">
                                                                <input v-model="language.profeciency_level" type="text"
                                                                    id="profeciency_level" class="form-control border-primary"
                                                                    placeholder="Proficiency Level" name="profeciency_level" required>
                                                                <span class="invalid-feedback">Proficiency Level is
                                                                    required</span>
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

                                                    <button @click="deleteLanguage(language.language_id)"
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
    name: 'languageList',
    setup() {

        const languages = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;
        const router = useRouter();

        const getLanguage = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/language/`);
                languages.value = response.data;
            } catch (error) {
                console.error('Error fetching languages:', error);
            }
        };

        const updateLanguage = async (languageIndex) => {
            try {
                await axios.patch(
                    `/user/${languageIndex.user_id}/language/${languageIndex.language_id}`,
                    languageIndex
                ).then(function (response) {
                    console.log(response);
                    router.push('/resume/language');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteLanguage = async (language_id) => {
            try {
                await axios.delete(`/user/${user_id}/language/${language_id}`);
                getLanguage();
            } catch (error) {
                console.error('Error deleting language:', error);
            }
        };

        const submitLanguageForm = async (languageIndex) => {
            const languageToUpdate = languages.value[languageIndex];
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            updateLanguage(languageToUpdate);
        };

        onMounted(() => {
            getLanguage();
        });

        return {
            languages,
            deleteLanguage,
            submitLanguageForm
        };
    },
});
</script>
  
<style></style>
  