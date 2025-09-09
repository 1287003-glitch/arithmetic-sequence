import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The arithmetic sequence as a list of numbers
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title and description
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term",
            value=1.0,
            step=1.0,
            help="The first number in the arithmetic sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (max 1000)"
        )
    
    # Input validation
    if num_terms <= 0:
        st.error("Number of terms must be a positive integer.")
        return
    
    if num_terms > 1000:
        st.error("Number of terms cannot exceed 1000 for performance reasons.")
        return
    
    # Generate sequence
    try:
        sequence = generate_arithmetic_sequence(first_term, common_difference, int(num_terms))
        
        # Display results section
        st.header("Generated Sequence")
        
        # Show sequence formula
        st.subheader("Formula")
        st.latex(f"a_n = {first_term} + (n-1) \\times {common_difference}")
        
        # Display sequence information
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("First Term", f"{first_term}")
        with col2:
            st.metric("Common Difference", f"{common_difference}")
        with col3:
            st.metric("Number of Terms", f"{int(num_terms)}")
        
        # Display the sequence
        st.subheader("Sequence")
        
        # Format sequence for display
        if len(sequence) <= 50:
            # For smaller sequences, display inline
            sequence_str = ", ".join([f"{term:g}" for term in sequence])
            st.code(sequence_str, language=None)
        else:
            # For larger sequences, display in a more compact format
            st.write(f"**First 10 terms:** {', '.join([f'{term:g}' for term in sequence[:10]])}")
            if len(sequence) > 20:
                st.write(f"**Last 10 terms:** {', '.join([f'{term:g}' for term in sequence[-10:]])}")
            
            # Show full sequence in expandable section
            with st.expander("Show complete sequence"):
                # Display in chunks for better readability
                chunk_size = 20
                for i in range(0, len(sequence), chunk_size):
                    chunk = sequence[i:i+chunk_size]
                    chunk_str = ", ".join([f"{term:g}" for term in chunk])
                    st.text(f"Terms {i+1}-{min(i+chunk_size, len(sequence))}: {chunk_str}")
        
        # Additional information
        st.subheader("Sequence Properties")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sum of all terms", f"{sum(sequence):g}")
        with col2:
            if len(sequence) > 1:
                st.metric("Last term", f"{sequence[-1]:g}")
            else:
                st.metric("Last term", f"{sequence[0]:g}")
        
        # Download option for large sequences
        if len(sequence) > 10:
            sequence_text = "\n".join([f"Term {i+1}: {term:g}" for i, term in enumerate(sequence)])
            st.download_button(
                label="📥 Download sequence as text file",
                data=sequence_text,
                file_name=f"arithmetic_sequence_{first_term}_{common_difference}_{num_terms}.txt",
                mime="text/plain"
            )
    
    except Exception as e:
        st.error(f"An error occurred while generating the sequence: {str(e)}")
    
    # Additional information section
    st.markdown("---")
    st.markdown("""
    ### About Arithmetic Sequences
    An arithmetic sequence is a sequence of numbers where the difference between consecutive terms is constant. 
    This difference is called the **common difference**.
    
    **General formula:** aₙ = a₁ + (n-1) × d
    
    Where:
    - aₙ is the nth term
    - a₁ is the first term
    - d is the common difference
    - n is the term number
    """)

if __name__ == "__main__":
    main()
