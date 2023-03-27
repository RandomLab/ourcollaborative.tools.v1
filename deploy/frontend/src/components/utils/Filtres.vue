<script setup>
    
    import { ref } from 'vue'
    import { storeToRefs } from 'pinia'
    import { useRouter, useRoute } from 'vue-router'
    
    import { useProjetStore } from '../../store/projects'

    const { projects, loading, error } = storeToRefs(useProjetStore())

    const { triAlpha, filterBy } = useProjetStore()


    const selectedAlpha = ref("asc")

    const selectedTemporality = ref("temporality")
    const selectedUsage = ref("usage")
    const selectedEnv = ref("environment")
    const selectedYear = ref("year")


    const router = useRouter()
    const route = useRoute()


    function changeAlpha(e) {
        console.log(selectedAlpha.value)
        triAlpha(selectedAlpha.value)
    }

    function changeTemporality(e) {
        if (selectedTemporality.value !== "temporality") {
            // router.replace({ name:'temporality', params: { name: selectedTemporality.value }})
            filterBy()
        }
    }

    function changeUsage(e) {
        if (selectedUsage.value !== "usage") {
            router.replace({ name:'usage', params: { name: selectedUsage.value }})
        }
    }

    function changeEnv(e) {
        if (selectedEnv.value !== "environment") {
            router.replace({ name:'environment', params: { name: selectedEnv.value }})
        }
    }

    function changeYear(e) {
        if (selectedYear.value !== "year") {
            router.replace({ name:'year', params: { year: selectedYear.value }})
        }
    }
    
</script>

<template>
    
    <div class="filtres">

        <select v-model="selectedAlpha" @change="changeAlpha">
            <option value="asc">Asc</option>
            <option value="desc">Desc</option>
        </select>

        <select v-model="selectedTemporality" @change="changeTemporality">
            <option value="temporality">Temporality</option>
            <option value="event">Event</option>
            <option value="continuous">Continuous</option>
        </select>

        <select v-model="selectedUsage" @change="changeUsage">
            <option value="usage">Usage</option>
            <option value="collaboration">Collaboration</option>
            <option value="cooperation">Cooperation</option>
            <option value="contribution">Contribution</option>
            <option value="participatory">Participatory</option>
        </select>

        <select v-model="selectedEnv" @change="changeEnv">
            <option value="environment">Environment</option>
            <option value="web">Web</option>
            <option value="desktop">Desktop</option>
            <option value="mobile">Mobile</option>
        </select>

        <select v-model="selectedYear" @change="changeYear">
            <option value="year">Year</option>
            <option value="1980">1980</option>
            <option value="1981">1981</option>
            <option value="1982">1982</option>
            <option value="1983">1983</option>
            <option value="1984">1984</option>
            <option value="1985">1985</option>
            <option value="1986">1986</option>
            <option value="1987">1987</option>
            <option value="1988">1988</option>
            <option value="1989">1989</option>
            <option value="1990">1990</option>
            <option value="1991">1991</option>
            <option value="1992">1992</option>
            <option value="1993">1993</option>
            <option value="1994">1994</option>
            <option value="1995">1995</option>
            <option value="1996">1996</option>
            <option value="1997">1997</option>
            <option value="1998">1998</option>
            <option value="1999">1999</option>
            <option value="2000">2000</option>
            <option value="2001">2001</option>
            <option value="2002">2002</option>
            <option value="2003">2003</option>
            <option value="2004">2004</option>
            <option value="2005">2005</option>
            <option value="2006">2006</option>
            <option value="2007">2007</option>
            <option value="2008">2008</option>
            <option value="2009">2009</option>
            <option value="2010">2010</option>
            <option value="2011">2011</option>
            <option value="2012">2012</option>
            <option value="2013">2013</option>
            <option value="2014">2014</option>
            <option value="2015">2015</option>
            <option value="2016">2016</option>
            <option value="2017">2017</option>
            <option value="2018">2018</option>
            <option value="2019">2019</option>
            <option value="2020">2020</option>
            <option value="2021">2021</option>
            <option value="2022">2022</option>
            <option value="2023">2023</option>
        </select>

    </div>
</template>