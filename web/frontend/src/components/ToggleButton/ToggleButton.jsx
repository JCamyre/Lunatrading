import styled from 'styled-components';
import style from 'styled-theming';

const getBackground = style.variants('mode', 'variant', {
    normal: {
        light: '#EEE',
        dark: '#111'
    },
    primary: {
        light: 'papayawhip',
        dark: 'pink'
    }
});

const ToggleButton = styled.button`
    background-color: ${getBackground}
`;

export default ToggleButton