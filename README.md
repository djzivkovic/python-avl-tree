# AVL Tree Implementation

This repository contains a Python implementation of an AVL (Adelson-Velsky and Landis) tree, which is a self-balancing binary search tree. It is a part of a university project for the 2nd-year Data Structures and Algorithms course.

## Table of Contents
- [Introduction](#introduction)
- [Methods](#methods)
- [Usage](#usage)
- [Sample Usage](#sample-usage)

## Introduction

An AVL tree is a self-balancing binary search tree, where the heights of the two child subtrees of every node differ by at most one. When a new node is inserted or an existing node is deleted, the tree is rebalanced to maintain this property, making it efficient for various operations.

This implementation includes the following classes:
- `Node`: Represents a node in the AVL tree with a value, left child, right child, and height.
- `EdgePrinter`: A helper class to print the tree structure.
- `AVLTree`: The main AVL tree class that supports insertion and deletion of nodes while maintaining the AVL property.

## Methods

```python
insert_node(key)
```
Insert a new node with the specified key into the AVL tree. The tree will be automatically balanced if needed.

```python
delete_node(key)
```
Delete the node with the specified key from the AVL tree. The tree will be automatically balanced if needed.
```python
print_tree()
```
Print the current state of the AVL tree. This function shows the structure of the tree.

## Usage

To use this AVL tree implementation, you can create an instance of the `AVLTree` class and then insert and delete nodes as needed. Here's how to use it:
 ```python
 tree = AVLTree()
 tree.insert_node(key)
 tree.delete_node(key)
 ```

## Sample Usage
Here's an example of how you can interact with the AVL tree using the provided command-line interface:
```
Insert: /i <key>
Delete: /d <key>
Quit: /q
```
