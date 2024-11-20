package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Main application class for the Hello World Spring Boot Application.
 */
@SpringBootApplication
public class App {

    /**
     * The main method - entry point for the Spring Boot application.
     *
     * @param args command line arguments.
     */
    public static void main(final String[] args) {
        SpringApplication.run(App.class, args);
    }
}

/**
 * REST Controller to handle the root endpoint.
 */
@RestController
class HelloController {

    /**
     * Handles the root (/) GET request and returns "Hello, World!".
     *
     * @return A simple Hello World message.
     */
    @GetMapping("/")
    public String hello() {
        return "Hello, World!";
    }
}
