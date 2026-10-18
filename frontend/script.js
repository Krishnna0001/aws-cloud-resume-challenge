"use strict";

document.addEventListener("DOMContentLoaded", async () => {
    const counter = document.getElementById("visitor-count");

    if (!counter) {
        console.error("Visitor counter element was not found.");
        return;
    }

    const API_URL =
        "https://9u7sc7qjg1.execute-api.ap-south-1.amazonaws.com/visitor-count";

    counter.textContent = "Loading visitor count...";

    try {
        const response = await fetch(API_URL, {
            method: "GET",
            cache: "no-store"
        });

        if (!response.ok) {
            throw new Error(`API request failed: HTTP ${response.status}`);
        }

        const data = await response.json();

        if (typeof data.visitorCount !== "number") {
            throw new Error("Invalid visitor count received from API.");
        }

        counter.textContent = data.visitorCount.toLocaleString();
        console.log("AWS visitor counter connected successfully.");

    } catch (error) {
        counter.textContent = "Temporarily unavailable";
        console.error("Visitor counter error:", error);
    }
});
