const cityInput = document.getElementById("cityInput");
const searchButton = document.getElementById("searchButton");
const weatherCard = document.getElementById("weatherCard");
const agentText = document.getElementById("agentText");

searchButton.addEventListener("click", handleSearch);

cityInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        handleSearch();
    }
});

async function handleSearch() {
    const city = cityInput.value.trim();

    if (!city) {
        agentText.textContent =
            "Please enter a city name so I can check its weather.";
        return;
    }

    searchButton.disabled = true;
    searchButton.querySelector("span").textContent = "Checking...";

    agentText.textContent =
        `Checking the latest weather for ${city}...`;

    try {
        const response = await fetch(
            `/weather?city=${encodeURIComponent(city)}`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to get weather.");
        }

        document.getElementById("location").textContent =
            `${data.city}, ${data.country}`;

        document.getElementById("temperature").textContent =
            data.temperature;

        document.getElementById("feelsLike").textContent =
            data.feels_like;

        document.getElementById("humidity").textContent =
            `${data.humidity}%`;

        document.getElementById("precipitation").textContent =
            `${data.precipitation} mm`;

        document.getElementById("windSpeed").textContent =
            `${data.wind_speed} km/h`;

        document.getElementById("condition").textContent =
            data.condition;

        document.getElementById("weatherIcon").textContent =
            data.icon;

        document.getElementById("date").textContent =
            "Current weather";

        agentText.textContent =
            `Here is the latest weather information for ${data.city}.`;

        weatherCard.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

    } catch (error) {

        agentText.textContent = error.message;

    } finally {

        searchButton.disabled = false;
        searchButton.querySelector("span").textContent = "Get Weather";
    }
}