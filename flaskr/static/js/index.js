function onShowModal(el, attributeToKeyMap= {}, name = '#staticBackdrop') {
  let json = JSON.parse(el.getAttribute('data-bs-json'));
  let elementsWithName = document.querySelectorAll(name + ' [name]');

  // Loop through the NodeList and update value
  elementsWithName.forEach(function (element) {
    // Define a mapping of attribute names to JSON keys
    // const attributeToKeyMap = {
    //   businessid: 'BusinessID',
    //   customerid: 'CustomerID',
    //   name: 'CustomerName',
    //   email: 'Email',
    //   phone: 'Phone',
    //   industry: 'Industry',
    //   location: 'Location'
    // };

    // Iterate over each attribute and set its value from the JSON object
    for (const attributeName in attributeToKeyMap) {
      if (element.getAttribute('name') === attributeName) {
        element.value = json[attributeToKeyMap[attributeName]];
        break; // Exit loop after setting the value
      }
    }
  });
  return;
}
