const BASE_JS_PATH = '../../../../../cfgov/unprocessed/js/';
const atomicHelpers = require( BASE_JS_PATH + 'modules/util/atomic-helpers' );
const Footer = require(
  BASE_JS_PATH + 'organisms/Footer'
);

let containerDom;
let componentDom;
const testClass = 'o-footer';
const HTML_SNIPPET = `
  <div class="container">
    <div class="o-footer"></div>
    <div class="o-footer"></div>
  </div>
`;

describe( 'atomic-helpers', () => {
  beforeEach( () => {
    document.body.innerHTML = HTML_SNIPPET;
    containerDom = document.querySelector( '.container' );
    componentDom = document.querySelector( `.${ testClass }` );
  } );

  describe( '.checkDom()', () => {
    it( 'should throw an error if element DOM not found', () => {
      const errMsg = 'null is not valid. ' +
                     'Check that element is a DOM node with ' +
                     `class ".${ testClass }"`;
      function errFunc() {
        atomicHelpers.checkDom( null, testClass );
      }
      expect( errFunc ).toThrow( Error, errMsg );
    } );

    it( 'should throw an error if element class not found', () => {
      const errMsg = 'mock-class not found on or in passed DOM node.';
      function errFunc() {
        atomicHelpers.checkDom( componentDom, 'mock-class' );
      }
      expect( errFunc ).toThrow( Error, errMsg );
    } );

    it( 'should return the correct HTMLElement when direct element is searched',
      () => {
        const dom = atomicHelpers.checkDom( componentDom, testClass );
        expect( dom ).toStrictEqual( componentDom );
      }
    );

    it( 'should return the correct HTMLElement when parent element is searched',
      () => {
        const dom = atomicHelpers.checkDom( containerDom, testClass );
        expect( dom ).toStrictEqual( componentDom );
      }
    );
  } );

  describe( '.instantiateAll()', () => {
    it( 'should return an array of instances', () => {
      const instArr = atomicHelpers.instantiateAll(
        `.${ testClass }`, Footer
      );
      expect( instArr ).toBeInstanceOf( Array );
      expect( instArr.length ).toBe( 2 );
    } );
  } );

  describe( '.setInitFlag()', () => {
    it( 'should return true when init flag is set', () => {
      expect( atomicHelpers.setInitFlag( componentDom ) ).toBe( true );
    } );

    it( 'should return false when init flag is already set', () => {
      atomicHelpers.setInitFlag( componentDom );
      expect( atomicHelpers.setInitFlag( componentDom ) ).toBe( false );
    } );
  } );

  describe( '.destroyInitFlag()', () => {

    beforeEach( () => {
      atomicHelpers.setInitFlag( componentDom );
    } );

    it( 'should return true when init flag is removed', () => {
      expect( atomicHelpers.destroyInitFlag( componentDom ) ).toBe( true );
    } );

    it( 'should return false when init flag has already been removed', () => {
      atomicHelpers.destroyInitFlag( componentDom );
      expect( atomicHelpers.destroyInitFlag( componentDom ) ).toBe( false );
    } );
  } );
} );
