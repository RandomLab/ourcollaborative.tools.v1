<script setup>

    import { marked } from 'marked'
    import { storeToRefs } from 'pinia'

    import { useInformationsStore } from '../store/informations'

    import Logos from '../components/utils/Logos.vue'

    const { informations, loading, error } = storeToRefs(useInformationsStore())

    const { fetchInformations } = useInformationsStore()

    fetchInformations()

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div v-if="informations" class="information">
            <li 
                v-for="information in informations"
                :key="information.id"
            >   
                <h1>{{ information.title }}</h1>
                <p v-html="marked.parse(information.text)"></p>

            </li>


        </div>
    <logos
        width="900" 
        height="190"
    ></logos>
    </main>
</template>