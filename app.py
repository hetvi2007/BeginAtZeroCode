import streamlit as st

# --- App Title ---
st.set_page_config(page_title="BeginAtZeroCode", layout="wide")
st.title("👨‍💻 BeginAtZeroCode")
st.subheader("Learn programming languages from scratch")

# --- Sidebar ---
st.sidebar.title("📚 Select Language")
language = st.sidebar.selectbox(
    "Choose a programming language:",
    ["Python", "C", "C++", "Java", "C#"]
)

# --- Lesson Content ---
st.markdown("---")
st.header(f"🔤 {language} - Introduction")

if language == "Python":
    st.write("""
    Python is a high-level, interpreted programming language known for its simplicity and readability.

    **Hello World Example:**
    ```python
    print("Hello, World!")
    ```
    """)

elif language == "C":
    st.write("""
    C is a powerful system programming language that is close to hardware.

    **Hello World Example:**
    ```c
    #include <stdio.h>
    
    int main() {
        printf("Hello, World!");
        return 0;
    }
    ```
    """)

elif language == "C++":
    st.write("""
    C++ is an extension of C with object-oriented features.

    **Hello World Example:**
    ```cpp
    #include <iostream>
    using namespace std;

    int main() {
        cout << "Hello, World!";
        return 0;
    }
    ```
    """)

elif language == "Java":
    st.write("""
    Java is a platform-independent object-oriented language.

    **Hello World Example:**
    ```java
    public class Main {
        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }
    ```
    """)

elif language == "C#":
    st.write("""
    C# is a modern, object-oriented language developed by Microsoft.

    **Hello World Example:**
    ```csharp
    using System;

    class Program {
        static void Main() {
            Console.WriteLine("Hello, World!");
        }
    }
    ```
    """)


