# Project Title

## Introduction

This project aims to fuzz the DataFrame instance methods from Pandas library this will ultimately allow us to spot bugs or any undesirable behavior like hangs and crashes. Paralerly we are able to capture different metrics related to the fuzzing campaing specifically code coverage, bug rate, memory and cpu usage and time per cycle.

## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Target Class and Description](#target-class-and-description)
- [Results](#results)
- [Oracle Structure](#oracle-structure)

## Description

The project is a testing framework that leverages fuzzing techniques to test the functionality and performance of the pandas library. It provides a systematic approach to generate diverse inputs and compare the outputs against a reference implementation of pandas, known as the healthy pandas, to ensure correctness and reliability.

## Target Class and Description

The target class in the project is the DataFrame class in the pandas library. The DataFrame class is a fundamental data structure in pandas that represents a tabular, spreadsheet-like data structure containing rows and columns. It provides powerful data manipulation and analysis capabilities, making it a critical component of the library.

The purpose of the target class is to provide a flexible and efficient way to work with structured data. It supports various operations such as indexing, filtering, merging, aggregating, and more. The DataFrame class is designed to handle both small and large datasets, making it suitable for a wide range of data analysis tasks.

## Results

The project has achieved significant insights into the behavior and performance of various pandas methods under different input scenarios. The results highlight potential bugs, corner cases, and performance bottlenecks that can be further investigated and addressed by the pandas development team. By running extensive tests and comparing the outputs with the healthy pandas implementation, the project contributes to improving the overall quality and reliability of the pandas library.

## Oracle Structure

The oracles in the project serve the purpose of validating the correctness and consistency of the pandas library. They capture various metrics and properties, including input-output comparisons, performance measurements, and functional behavior checks. The oracles are designed to detect discrepancies between the actual pandas implementation and the healthy pandas implementation, providing valuable insights into potential issues or inconsistencies in the library.
